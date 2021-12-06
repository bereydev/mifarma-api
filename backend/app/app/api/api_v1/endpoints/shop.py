from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic.types import UUID4
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/catalog/", response_model=List[schemas.Product])
def read_catalog(
    filter: str = "",
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Get the catalog of product from the customer's pharamcy
    """
    if current_user.pharmacy_id is None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="This user has has no pharmacy"
        )
        
    catalog = crud.product.get_multi_by_pharmacy(db, skip=skip, limit=limit, filter=filter, pharmacy_id=current_user.pharmacy_id)
    return catalog


@router.post("/add-to-cart/{product_id}", response_model=schemas.Order)
def add_to_cart(
    product_id: UUID4,
    amount: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Add a product to the user card
    """
    if not current_user.is_customer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user does not have the requested permissions",
        )
    
    if current_user.pharmacy_id is None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="This user has has no pharmacy"
        )

    product = crud.product.get(db, product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Requested product does not exist in db",
        )

    # Check if an order  with the same product already exist in the user cart
    order = crud.order.get_duplicate_in_cart(db=db, user_id=current_user.id, product_id=product_id)
    
    if order is None:
        order = crud.order.create(db=db, obj_in=schemas.OrderCreate(product_id=product_id, amount=amount, pharmacy_id=current_user.pharmacy_id, user_id=current_user.id))
    else:
        # Add amount to the existing order
        order = crud.order.add_items(db=db, obj_in=order, amount=amount)
    
    return order

@router.delete("/delete-from-cart/{order_id}", response_model=List[schemas.Order])
def delete_from_cart(
    order_id: UUID4,
    amount: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Add a product to the user card
    """
    if not current_user.is_customer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user does not have the requested permissions",
        )

    if current_user.pharmacy_id is None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="This user has has no pharmacy"
        )

    order = crud.order.get(db=db, id=order_id)
    
    if order is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Requested order does not exist in db",
        )
    
    new_amount = order.amount - amount
    
    if new_amount == 0:
        crud.order.remove(db, id=order_id)
    elif order.amount >= amount and amount > 0:
        order = crud.order.update(
            db=db, 
            db_obj=order, 
            obj_in=schemas.OrderUpdate(amount=new_amount)
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="The amount to delete from order is negative or too large"
        )
    return current_user.get_cart()

@router.post("/place-order", response_model=List[schemas.Order])
def place_order(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Place an order on the currently in cart item 
    -> change the OderRecords status from in_cart to in_process
    """
    if not current_user.is_customer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user does not have the requested permissions",
        )
    
    if current_user.pharmacy_id is None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="This user has has no pharmacy"
        )

    cart = current_user.get_cart()
    if cart is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The current_user has an empty cart",
        )
    cart = crud.order.place_order(db=db, user_obj=current_user)

    return cart


@router.get("/get-cart", response_model=List[schemas.Order])
def get_cart(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Get the  of order in the cart of the current user
    """    
    if not current_user.is_customer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user does not have the requested permissions",
        )
    
    if current_user.pharmacy_id is None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="This user has has no pharmacy"
        )

    return current_user.get_cart()


@router.get('/order/history', response_model=List[schemas.Order])
def get_order_history(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_user),
    ) -> Any:
    """Get previously placed orders order by type and by descending date"""
    if not current_user.is_customer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user does not have the requested permissions",
        )
    
    if current_user.pharmacy_id is None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="This user has has no pharmacy"
        )
    
    placed_orders = crud.order.get_history_order_by_status(db=db, skip=skip, limit=limit, customer=current_user)
    return placed_orders