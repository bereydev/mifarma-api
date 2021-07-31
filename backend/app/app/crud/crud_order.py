from app.models.ordercontent import OrderContentStatus
from app.api.api_v1.endpoints.shop import place_order
from app.models.order import OrderStatus
from typing import List, Optional
from typing_extensions import runtime
from pydantic.types import UUID4
from sqlalchemy.orm import Session
from sqlalchemy import true, false, or_, and_
from fastapi import HTTPException, status
from .base import CRUDBase
from app.models import Order, OrderStatus, User
from app.models.role import RoleName
from app.schemas import OrderCreate, OrderUpdate
from . import user


class CRUDOrder(CRUDBase[Order, OrderCreate, OrderUpdate]):
    def place_order(self, db: Session, order_obj: Order) -> Order:
        order_obj.status = OrderStatus.placed
        for order_content in order_obj.content:
            order_content.status = OrderContentStatus.in_process
        db.commit()
        db.refresh(order_obj)
        return order_obj

    def get_history_order_by_status(self, db: Session, *, skip: int, limit: int, customer: User) -> List[Order]:
        return (customer.orders
                .filter(Order.status != OrderStatus.in_cart)
                .order_by(Order.status, Order.order_date.desc())
                .offset(skip).limit(limit).all())

    def get_multi_placed(self, db: Session, *, skip: int, limit: int, descending: bool = False) -> List[Order]:
        placed_orders = db.query(self.model).filter(Order.status == OrderStatus.placed)
        placed_orders = placed_orders.order_by(Order.order_date.desc(
        )) if descending else placed_orders.order_by(Order.order_date)
        return placed_orders.offset(skip).limit(limit).all()

    def get_multi_placed_by_customer(self, db: Session, *, skip: int, limit: int, customer_id: UUID4, descending: bool = False) -> List[Order]:
        customer = user.get(db, customer_id)
        if customer is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No such user"
            )
        if not customer.is_customer:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="User is not a customer",
            )
        placed_orders = db.query(self.model).filter(
            Order.user_id == customer_id).filter(Order.status == OrderStatus.placed)

        placed_orders = placed_orders.order_by(Order.order_date.desc(
        )) if descending else placed_orders.order_by(Order.order_date)

        return placed_orders.offset(skip).limit(limit).all()


order = CRUDOrder(Order)
