from app.schemas import order
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic.types import UUID4
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get('/placed-orders')
def get_placed_orders(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_user),
    descending: bool = False
    ) -> Any:
    """Get the placed orders"""
    if not (current_user.is_owner or current_user.is_admin):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Don't have enough permissions",
        )
    placed_orders = crud.order.get_multi_placed(
        db=db, skip=skip, limit=limit, descending=descending)
    return placed_orders


@router.get('/placed-orders-by-customer/{customer_id}')
def get_placed_orders_by_customer(
    customer_id: UUID4,
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_user),
    descending: bool = False
    ) -> Any:
    """Get the placed orders or a given customer"""
    if not (current_user.is_owner or current_user.is_admin):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Don't have enough permissions",
        )
    placed_orders = crud.order.get_multi_placed_by_customer(
        db=db, skip=skip, limit=limit, customer_id=customer_id, descending=descending)
    return placed_orders


@router.put('/update-ordercontent-status/{ordercontent_id}')
def update_ordercontent_status(
    ordercontent_id: UUID4,
    ordercontent_status: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
    ) -> Any:
    """ Update the ordercontent status to make change its status"""
    if not (current_user.is_owner or current_user.is_admin):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Don't have enough permissions",
        )

    ordercontent = crud.ordercontent.get(db, ordercontent_id)
    if ordercontent is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No such ordercontent"
            )

    # Allow to edit only the pharmacy's customer's orders
    if ordercontent.order.user.pharmacy_id != current_user.pharmacy_id:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Customer is not a client of the pharmacy"
            )

    ordercontent = crud.ordercontent.update_status(db, ordercontent, ordercontent_status)

    return ordercontent


@router.get('/order/{order_id}', response_model=schemas.Order)
def get_order(
    order_id: UUID4,
    current_user: models.User = Depends(deps.get_current_user),
    db: Session = Depends(deps.get_db),
    ) -> Any:
    """Get the details of the order and the ordercontent elements"""
    if not (current_user.is_owner or current_user.is_admin):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Don't have enough permissions",
            )
    order = crud.order.get(db, order_id)
    return order