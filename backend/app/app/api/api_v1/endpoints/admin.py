from starlette.types import Scope
from app.models import pharmacy, stock_item
from random import randint
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm.session import Session
from pydantic.types import UUID4

from app import crud, models, schemas
from app.api import deps
from app.core.celery_app import celery_app
from app.utils import send_test_email, send_new_account_email
from app.models.role import Role, RoleName

router = APIRouter()

@router.post("/user", response_model=schemas.User)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserCreate,
    role: str,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> Any:
    """
    [ADMIN] Create new user.
    """
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The current user has not enough permissions.",
        )
    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user with this username already exists in the system.",
        )
    if role not in vars(RoleName).values():
        raise HTTPException(
            status_code=404,
            detail="Requested Role does not exist in db",
        )
    if role == RoleName.ADMIN:
        user = crud.user.create_admin(db, user_in)
    elif role == RoleName.OWNER:
        user = crud.user.create_owner(db, user_in)
    elif role == RoleName.EMPLOYEE:
        user = crud.user.create_employee(db, user_in)
    else:
        user = crud.user.create_customer(db, user_in)

    send_new_account_email(
        email_to=user_in.email, username=user_in.email, password=user_in.password
    )
    return user


@router.put("/user/{user_id}", response_model=schemas.User)
def update_user(
    *,
    db: Session = Depends(deps.get_db),
    user_id: UUID4,
    user_in: schemas.UserUpdate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> Any:
    """
    [ADMIN] Update a user by id.
    """
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    user = crud.user.update(db, db_obj=user, obj_in=user_in)
    return user


@router.get("/user/{user_id}", response_model=schemas.User)
def read_user_by_id(
    user_id: UUID4,
    current_user: models.User = Depends(deps.get_current_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    [ADMIN] Get a specific user by id.
    """
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user doesn't have enough permissions"
        )

    user = crud.user.get(db, id=user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No user found with this id"
        )
    return user


@router.put("/verify-owner/{id}", response_model=schemas.OwnerActivation)
def verify_owner(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
    id: UUID4,
) -> Any:
    """
    [ADMIN] Verify the user after a manual check for its identity and its pharmacy_number
    """
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user has not enaught privileges",
        )
    # TODO send a letter to check the address (with a token to be sure that the user is the pharmacist)
    user = crud.user.get(db, id)
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="No user linked to the requested id",
        )
    if not user.is_owner:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The requested user is not an owner",
        )
    if user.verified:
        activation_token = 1234
    else:
        activation_token = randint(1_000,9_999)
        
    user = crud.user.verify(db, user)
    print(user.email)
    data_user = jsonable_encoder(user)

    return schemas.OwnerActivation(**data_user, role=user.role, activation_token=activation_token)


@router.post("/pharmacy/{user_id}", response_model=schemas.Pharmacy)
def create_pharmacy(
    *,
    user_id: UUID4,
    db: Session = Depends(deps.get_db),
    pharmacy_in: schemas.PharmacyCreate,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Create new pharmacy with owner.
    """
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User has not enough premissions"
        )

    user = crud.user.get(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with specified id does not exist",
        )
    if user.is_owner and user.pharmacy_id is None:
        pharmacy = crud.pharmacy.create(db=db, obj_in=pharmacy_in)
        pharmacy.users.append(crud.user.get(db, current_user.id))
        db.commit()
    elif user.pharmacy_id is not None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="User has already a pharmacy",
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Provided user is not an owner",
        )
    return pharmacy


@router.post("/catalog")
def update_catalog(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Update the drug catalog from a CSV/EXCEL file
    """
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions")
    # TODO parse the document
    return {'success': True, 'msg': 'The catalog is successfully updated'}


@router.post("/drug", response_model=schemas.Drug)
def create_drug(
    *,
    db: Session = Depends(deps.get_db),
    drug_in: schemas.DrugCreate,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Create new drug in the catalog [only for test purposes].
    """
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Don't have enaught permission to add drug to the catalog",
        )
    if current_user.pharmacy_id is not None:
        drug= crud.drug.create(db=db, obj_in=drug_in)
        # product = crud.product.create_from_drug_with_pharmacy(db=db, db_drug=drug, pharmacy_id=current_user.pharmacy_id)
    else:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Current user has no attributed pharmacy",
        )
    return drug


@router.post("/drug/{product_id}/pharmacy/{pharmacy_id}", response_model=schemas.StockItem)
def add_drug_to_stock(
    *,
    product_id: UUID4,
    pharmacy_id: UUID4,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Add a drug to the catalog of a pharmacy.
    """
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Don't have enaught permission to add drug to the catalog",
        )
    product = crud.drug.get(db, product_id)
    pharmacy = crud.pharmacy.get(db, pharmacy_id)
    
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Drug with the given id does not exist"
        )
    
    if pharmacy is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pharmacy with the given id does not exist"
        )

    # Create a stock item
    stock_item = crud.stock_item.create_with_product_and_pharmacy(db, product_id=product_id, pharmacy_id=pharmacy_id)
    pharmacy.stock_items.append(stock_item)
    db.commit()
    print(stock_item)
    return stock_item
