from random import randint
from typing import Any, List
from app.db.session import engine

from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm.session import Session
from pydantic.types import UUID4

from app import crud, models, schemas
from app.api import deps
from app.utils import send_new_account_email
from app.models.role import RoleName
import pandas as pd
import os
import shutil

router = APIRouter()


@router.post("/user", response_model=schemas.User)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserCreate,
    role: str,
        current_user: models.User = Depends(deps.get_current_superuser),) -> Any:
    """
    [ADMIN] Create new user.
    """
    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user with this username already exists in the system.",
        )
    if role not in vars(RoleName).values():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
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
        current_user: models.User = Depends(deps.get_current_superuser),) -> Any:
    """
    [ADMIN] Update a user by id.
    """
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The user with this username does not exist in the system",
        )
    user = crud.user.update(db, db_obj=user, obj_in=user_in)
    return user


@router.get("/user/{user_id}", response_model=schemas.User)
def read_user_by_id(
        user_id: UUID4,
        current_user: models.User = Depends(deps.get_current_superuser),
        db: Session = Depends(deps.get_db),) -> Any:
    """
    [ADMIN] Get a specific user by id.
    """
    user = crud.user.get(db, id=user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No user found with this id"
        )
    return user


@router.get("/customers", response_model=List[schemas.Customer])
def read_customers(
        current_user: models.User = Depends(deps.get_current_superuser),
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(deps.get_db),) -> Any:
    """
    [ADMIN] Get customers of mi farmacia
    """
    customers = crud.user.get_multi_by_role(
        db, skip=skip, limit=limit, role=RoleName.CUSTOMER)
    return customers


@router.get("/pharmacy/{pharmacy_id}/owner", response_model=schemas.User)
def read_pharmacy_owner(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_superuser),
    pharmacy_id: UUID4,
) -> Any:
    """
    [ADMIN] Get owner of the current_user's pharmacy
    """
    pharmacy = crud.pharmacy.get(db=db, id=pharmacy_id)
    if pharmacy is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No pharmacy linked to the requested pharmacy_id")

    return pharmacy.get_owner()


@router.put("/verify-owner/{owner_id}", response_model=schemas.OwnerActivation)
def verify_owner(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_superuser),
        owner_id: UUID4,) -> Any:
    """
    [ADMIN] Verify the user after a manual check for its identity and its pharmacy_number
    """
    # TODO send a letter to check the address (with a token to be sure that the user is the pharmacist)
    user = crud.user.get(db, owner_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No user linked to the requested owner_id",
        )
    if not user.is_owner:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The requested user is not an owner",
        )
    if user.verified:
        activation_token = 1234
    else:
        activation_token = randint(1_000, 9_999)

    user = crud.user.verify(db, user)
    print(user.email)
    data_user = jsonable_encoder(user)

    return schemas.OwnerActivation(**data_user, role=user.role, activation_token=activation_token)


@router.put("/full-activate-owner/{id}", response_model=schemas.User)
def full_activate_user(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_superuser),
    id: UUID4,
) -> Any:
    """
    [ADMIN] Set three verification status of a user to true (verified, confirmed, activated)
    """
    user = crud.user.get(db, id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No user linked to the requested id",
        )

    user = crud.user.verify(db, user)
    user = crud.user.activate(db, user)
    user = crud.user.confirm(db, user)

    return user


@router.post("/pharmacy/{user_id}", response_model=schemas.Pharmacy)
def create_pharmacy(
    *,
    user_id: UUID4,
    db: Session = Depends(deps.get_db),
    pharmacy_in: schemas.PharmacyCreate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> Any:
    """
    [ADMIN] Create new pharmacy with owner.
    """
    user = crud.user.get(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with specified id does not exist",
        )
    if user.is_owner and user.pharmacy_id is None:
        pharmacy = crud.pharmacy.create(db=db, obj_in=pharmacy_in)
        pharmacy.users.append(crud.user.get(db, user.id))
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
    excel_catalog: UploadFile = File(...),
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_superuser),
) -> Any:
    """
    [ADMIN] Update the drug catalog from a EXCEL file
    """
    # Get the uploaded excel documents
    # Parse it with pandas
    usecols = ['EAN', 'LABORATORIO', 'PRODUCTO']
    file_name = 'test.xlsx'
    with open(file_name, 'wb') as buffer:
        shutil.copyfileobj(excel_catalog.file, buffer)

    catalog_df = pd.read_excel(file_name, usecols=usecols)

    for row in catalog_df.iterrows():
        ean_code, laboratory, name = row[1]
        product = crud.product.get_by_ean(db, str(ean_code))
        if product is None:
            product_in = schemas.ProductCreate(ean_code=str(ean_code), laboratory=laboratory, name=name)
            crud.product.create(db, obj_in=product_in)
        else:
            product_in = schemas.ProductUpdate(laboratory=laboratory, name=name)
            crud.product.update(db, db_obj=product, obj_in=product_in)

    # Create objects in the database from excel
    os.remove(file_name)

    return {'success': True, 'msg': 'The catalog is successfully updated', 'filename': excel_catalog.filename,
            'file_type': excel_catalog.content_type}


@router.post("/drug", response_model=schemas.Drug)
def create_drug(
    *,
    db: Session = Depends(deps.get_db),
    drug_in: schemas.DrugCreate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> Any:
    """
    [ADMIN] Create new drug in the catalog [only for test purposes].
    """
    drug = crud.drug.create(db=db, obj_in=drug_in)
    return drug


@router.post("/product", response_model=schemas.Drug)
def create_product(
    *,
    db: Session = Depends(deps.get_db),
    product_in: schemas.ProductCreate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> Any:
    """
    [ADMIN] Create new product in the catalog [only for test purposes].
    """
    product = crud.product.create(db=db, obj_in=product_in)

    return product


@router.post("/stock_item", response_model=schemas.StockItem)
def create_stock_item(
    *,
    stock_item_in: schemas.StockItemCreate,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_superuser),
) -> Any:
    """
    [ADMIN] Add a product to the catalog of a pharmacy.
    """
    stock_item = crud.stock_item.create(db, obj_in=stock_item_in)
    return stock_item


@router.get("/catalog/{pharmacy_id}", response_model=List[schemas.Product])
def read_catalog(
    pharmacy_id: UUID4,
    filter: str = "",
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> Any:
    """
    [ADMIN] Get the catalog of product from a pharmacy by ID
    """
    catalog_content = crud.product.get_multi_by_pharmacy(
        db, skip=skip, limit=limit, filter=filter, pharmacy_id=pharmacy_id)
    return catalog_content


@router.get("/pharmacies/inactive", response_model=List[schemas.Pharmacy])
def read_inactive_pharmacys(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> Any:
    """
    Retrieve inactive pharmacies.
    """
    pharmacies = crud.pharmacy.get_multi_inactive(db, skip=skip, limit=limit)

    return pharmacies


@router.get("/owners/unverified", response_model=List[schemas.Owner])
def read_unverified_owners(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> Any:
    """
    Retrieve unverified owners.
    """
    owners = crud.user.get_multi_unverified(db, skip=skip, limit=limit)

    return owners
