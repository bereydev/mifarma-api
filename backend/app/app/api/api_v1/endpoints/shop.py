from app.models.order import OrderStatus
from app.schemas.ordercontent import OrderContentUpdate
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic.types import UUID4
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode

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
        
    catalog_content = crud.product.get_multi_by_pharmacy(db, skip=skip, limit=limit, filter=filter, pharmacy_id=current_user.pharmacy_id)
    return catalog_content


@router.post("/add-to-cart/{product_id}", response_model=schemas.OrderContent)
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
            status_code=404,
            detail="Requested product does not exist in db",
        )

    order = current_user.get_cart()
    ordercontent = None
    if order is None:
        order = crud.order.create(db=db, obj_in=schemas.OrderCreate(pharmacy_id=current_user.pharmacy_id, user_id=current_user.id, in_cart=True))
    else:
        # Check if an order content with the same product already exist in the user cart
        ordercontent = crud.ordercontent.get_duplicate_in_cart(db=db, user_id=current_user.id, product_id=product_id)
    
    if ordercontent is None:
        ordercontent = crud.ordercontent.create(db=db, obj_in=schemas.OrderContentCreate(order_id=order.id, product_id=product_id, amount=amount))
    else:
        # Add amount to the existing ordercontent
        ordercontent = crud.ordercontent.add_items(db=db, obj_in=ordercontent, amount=amount)
    
    return ordercontent

@router.delete("/delete-from-cart/{ordercontent_id}", response_model=schemas.OrderContent)
def delete_from_cart(
    ordercontent_id: UUID4,
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

    ordercontent = crud.ordercontent.get(db=db, id=ordercontent_id)
    
    if ordercontent is None:
        raise HTTPException(
            status_code=404,
            detail="Requested ordercontent does not exist in db",
        )
    
    new_amount = ordercontent.amount - amount
    
    if new_amount == 0:
        ordercontent = crud.ordercontent.remove(db, ordercontent_id)
    elif ordercontent.amount >= amount and amount > 0:
        ordercontent = crud.ordercontent.update(
            db=db, 
            db_obj=ordercontent, 
            obj_in=OrderContentUpdate(amount=new_amount)
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="The amount to delete from order is negative or too large"
        )
    return ordercontent

@router.post("/place-order", response_model=schemas.Order)
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

    order = current_user.get_cart()
    if order is None:
        raise HTTPException(
            status_code=404,
            detail="The current_user has an empty cart",
        )
    order = crud.order.place_order(db=db, order_obj=order)

    return order


@router.get("/get-cart", response_model=schemas.Order)
def get_cart(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Get the content of order in the cart of the current user
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


@router.get('/orders/history', response_model=List[schemas.Order])
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