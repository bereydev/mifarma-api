from app.models.role import Role, RoleName
from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from pydantic.types import UUID4
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings
from app.utils import generate_employee_invitation_token, send_employee_invitation_email, send_new_account_email, verify_employee_invitation_token
from random import randint

router = APIRouter()


@router.post("/", response_model=schemas.User)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserCreate,
    role: str,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> Any:
    """
    Create new user.
    """
    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    if role not in vars(RoleName).values():
        raise HTTPException(
            status_code=404,
            detail="Requested Role does not exist in db",
        )
    user = crud.user.create_with_role(db, obj_in=user_in, role=role)

    send_new_account_email(
        email_to=user_in.email, username=user_in.email, password=user_in.password
    )
    return user


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
    current_user_data = jsonable_encoder(current_user)
    user_in = schemas.UserUpdate(**current_user_data)
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


@router.post("/customer", response_model=schemas.User)
def create_customer(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserCreate
) -> Any:
    """
    Create new user without the need to be logged in.
    """

    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
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
            status_code=400,
            detail="The user with this username already exists in the system",
        )
    user = crud.user.create_owner(db, user_in)
    return user


@router.put("/activate-owner/{id}")
def activate_owner(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
    id: UUID4,
) -> Any:
    """
    Activate the user after a manual check for its identity and its pharmacy_number
    """
    if not current_user.is_admin:
        raise HTTPException(
            status_code=400,
            detail="The user has not enaught privileges",
        )
    # TODO send a letter to check the address (with a token to be sure that the user is the pharmacist)
    user = crud.user.get(db, id)
    user = crud.user.activate(db, user)
    return {'user': user.email,
    'verification_token': randint(1_000_000_000, 9_999_999_999)}


@router.post("/employee/accept-invitation", response_model=schemas.User)
def create_employee(
    *,
    token: str = Body(...),
    db: Session = Depends(deps.get_db),
    password: str = Body(...),
    email: EmailStr = Body(...),
    first_name: str = Body(None),
    last_name: str = Body(None),
) -> Any:
    """
    Create new employee if its invitation is valid.
    """
    pharmacy_id = verify_employee_invitation_token(token)
    if not pharmacy_id:
        raise HTTPException(status_code=400, detail="Invalid token")

    user = crud.user.get_by_email(db, email=email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system",
        )
    user_in = schemas.UserCreate(password=password, email=email, first_name=first_name,
                                 last_name=last_name, role_id=Role.get_role_id(RoleName.EMPLOYEE, db))
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
    if user == current_user:
        return user
    if not current_user.is_admin:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return user


@router.put("/{user_id}", response_model=schemas.User)
def update_user(
    *,
    db: Session = Depends(deps.get_db),
    user_id: UUID4,
    user_in: schemas.UserUpdate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> Any:
    """
    Update a user.
    """
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    user = crud.user.update(db, db_obj=user, obj_in=user_in)
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
            status_code=400, detail="The user doesn't have enough privileges"
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
