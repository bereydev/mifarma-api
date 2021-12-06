from app.models.user import User
from fastapi import HTTPException, status
from app.models.order import Order, OrderStatus
from typing import List, Optional
from pydantic.types import UUID4
from sqlalchemy.orm import Session
from sqlalchemy import and_
from .base import CRUDBase
from app.models import Order
from app.schemas import OrderCreate, OrderUpdate

class CRUDOrder(CRUDBase[Order, OrderCreate, OrderUpdate]):

    def place_order(self, db: Session, user_obj: User) -> Order:
        for order in user_obj.get_cart():
            order.status = OrderStatus.placed
        db.commit()
        db.refresh(user_obj)
        return user_obj.get_cart()

    def get_by_status(self, db: Session, customer_id: UUID4, status: OrderStatus) -> List[Order]:
        return db.query(self.model).filter(and_(Order.user_id == customer_id, Order.status == status)).all()
    
    def get_duplicate_in_cart(self, db: Session, user_id: UUID4, product_id: UUID4) -> Optional[Order]:
        return db.query(Order).filter(and_(Order.product_id == product_id, Order.status == OrderStatus.in_cart, Order.user_id == user_id)).first()

    def add_items(self, db: Session, obj_in: Order, amount: int) -> Order:
        obj_in.amount += amount
        db.commit()
        db.refresh(obj_in)
        return obj_in

    def update_status(self, db: Session, obj_in: Order, order_status: OrderStatus) -> Order:
        # Check if the status is a valid OrderStatus
        if not order_status in vars(OrderStatus).values():
            raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="The requested status does not exist",
            )
        obj_in.status = order_status
        db.commit()
        db.refresh(obj_in)
        return obj_in

    def get_history_order_by_status(self, db: Session, *, skip: int, limit: int, customer: User) -> List[Order]:
        orders = db.query(Order).filter(and_(Order.status != OrderStatus.in_cart, Order.user_id == customer.id)).order_by(Order.order_date.desc(), Order.status)
        return orders.offset(skip).limit(limit).all()


order = CRUDOrder(Order)