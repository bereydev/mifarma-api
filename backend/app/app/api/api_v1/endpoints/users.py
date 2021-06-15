from app.models.role import RoleName
from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from pydantic.types import UUID4
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.utils import generate_employee_invitation_token, send_employee_invitation_email, send_new_account_email, verify_employee_invitation_token
from random import randint

router = APIRouter()


@router.put("/me", response_model=schemas.User)
def update_user_me(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserUpdate,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Update own user.
    """
    user = crud.user.update(db, db_obj=current_user, obj_in=user_in)
    return user


@router.get("/me", response_model=schemas.User)
def read_user_me(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Get current user.
    """
    return current_user


@router.post("/customer", response_model=schemas.Customer)
def create_customer(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.CustomerCreate
) -> Any:
    """
    Create new user without the need to be logged in.
    """

    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="The user with this username already exists in the system",
        )
    user = crud.user.create_customer(db, user_in)
    return user


@router.post("/owner", response_model=schemas.User)
def create_owner(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.OwnerCreate
) -> Any:
    """
    Create new owner without the need to be logged in.
    """
    # TODO check if its a legit owner of a pharmacy
    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="The user with this username already exists in the system",
        )
    user = crud.user.create_owner(db, user_in)
    return user


@router.post("/employee/accept-invitation", response_model=schemas.Employee)
def create_employee(
    *,
    token: str,
    db: Session = Depends(deps.get_db),
    user_in: schemas.EmployeeCreate
) -> Any:
    """
    Create new employee if its invitation is valid.
    """
    pharmacy_id = verify_employee_invitation_token(token)
    if not pharmacy_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
            )

    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="The user with this username already exists in the system",
        )
    user = crud.user.create_employee(db, obj_in=user_in)
    pharmacy = crud.pharmacy.get(db, pharmacy_id)
    pharmacy.users.append(user)
    db.commit()
    return user


@router.get("/{user_id}", response_model=schemas.User)
def read_user_by_id(
    user_id: UUID4,
    current_user: models.User = Depends(deps.get_current_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    user = crud.user.get(db, id=user_id)
    # Can read Himself
    if user == current_user:
        return user
    # Employee and owners can read their clients
    # TODO can they read their previous clients ?
    if not user.pharmacy_id == current_user.pharmacy_id or not (current_user.is_owner or current_user.is_employee):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user doesn't have enough privileges to read this user data"
        )
    return user


@router.post("/employee-invitations")
def send_employee_invitations(
    employee_emails: List[str],
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Send invitations to the employees.
    """
    if not current_user.is_owner:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user doesn't have enough privileges"
        )
    if current_user.pharmacy_id is None:
        raise HTTPException(
            status_code=422, detail="The owner has no linked pharmacy"
        )

    for email in employee_emails:
        # TODO check the format of an email
        # throw an error in case of bad formating
        token = generate_employee_invitation_token(pharmacy_id=current_user.pharmacy_id)
        send_employee_invitation_email(email_to=email, token=token)

    return {"success": True, "msg": "The invitations to the employees are sent"}
