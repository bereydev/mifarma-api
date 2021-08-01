from os import stat
from sqlalchemy.sql.operators import nullsfirst_op
from sqlalchemy.util.langhelpers import duck_type_collection
from app.models.user import User
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
    if not (current_user.is_owner or current_user.is_admin or current_user.is_employee):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Don't have enough permissions",
        )
    customer = crud.user.get(db, customer_id)
    if customer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The requested customer_id is not found in the db"
        )
    if not customer.is_employee:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="The requested user is not a customer"
        )
    if not current_user.is_admin and current_user.pharmacy_id != customer.pharmacy_id:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Requested user is not a client of the current_user pharmacy"
        )
    placed_orders = crud.order.get_multi_placed_by_customer(
        db=db, skip=skip, limit=limit, customer_id=customer_id, descending=descending)
    return placed_orders


@router.get('/customers-with-most-recent-placed-orders/', response_model=List[schemas.User])
def get_customers_with_most_recent_placed_orders(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_user),
    ) -> Any:
    """
    Provide the list of customers that placed an order 
    in the current_user's pharmacy order by the most recently placed order
    """
    if current_user.pharmacy_id is None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="This user has has no pharmacy"
        )

    if not (current_user.is_admin or current_user.is_employee or current_user.is_owner) :
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user does not have the requested permissions",
        )
    return crud.user.get_customers_with_most_recent_placed_orders(db, skip, limit, current_user.pharmacy_id)


@router.put('/update-ordercontent-status/{ordercontent_id}')
def update_ordercontent_status(
    ordercontent_id: UUID4,
    ordercontent_status: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
    ) -> Any:
    """ Update the ordercontent status to make change its status
    in_cart = 0
    in_process = 1
    available = 2
    not_available = 3
    cancelled = 4 
    delivered = 5
    """
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


@router.get("/user/{public_id}", response_model=schemas.User)
def read_user_by_public_id(
    public_id: str,
    current_user: models.User = Depends(deps.get_current_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by its public_id.
    """
    # Normalize public id to capital letters
    public_id = str.upper(public_id)
    user = crud.user.get_by_public_id(db, public_id=public_id)
    
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No user found with this public_id"
        )
    # Allow only to read customers from their pharmacy
    elif not user.is_customer and current_user.pharmacy_id == user.pharmacy_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Requested user is not a customer or is not a client of this pharmacy"
        )

    if current_user.is_admin:
        return user

    if not user.pharmacy_id == current_user.pharmacy_id or not (current_user.is_owner or current_user.is_employee):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user doesn't have enough privileges to read this user data"
        )

    return user