from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from pydantic.types import UUID4
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import current_date, current_user

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/customer/products", response_model=List[schemas.Product])
def read_products(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Get the catalog of product from the customer's pharamcy
    """
    products = crud.product.get_multi()
    return


@router.post("/add-to-cart/{product_id}", response_model=List[schemas.Product])
def add_to_cart(
    product_id: UUID4,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Add a product to the user card
    """
    if not current_user.is_customer:
        raise HTTPException(
            status_code=400,
            detail="The user does not have the requested permissions",
        )
    product = crud.product.get(db, product_id)
    user = crud.user.get(db, current_user.id)
    # TODO create a in_cart order recods and bind it to the user and the pharmacy
    db.commit()
    # TODO add the product to the card
    return product

@router.post("/place-order", response_model=List[schemas.Product])
def place_order(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Place an order on the currently in cart item 
    -> change the OderRecords status from in_cart to in_process
    """
    return 