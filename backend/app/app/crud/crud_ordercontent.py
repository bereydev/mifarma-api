from fastapi import HTTPException, status
from app.models.order import Order, OrderStatus
from typing import List, Optional
from pydantic.types import UUID4
from sqlalchemy.orm import Session
from sqlalchemy import true, false, or_, and_
from .base import CRUDBase
from app.models import OrderContent, Order
from app.models.ordercontent import  OrderContentStatus
from app.models.role import RoleName
from app.schemas import OrderContentCreate, OrderContentUpdate

class CRUDOrderContent(CRUDBase[OrderContent, OrderContentCreate, OrderContentUpdate]):

    def get_by_status(self, db: Session, user_id: UUID4, status: OrderContentStatus) -> List[OrderContent]:
        return db.query(self.model).filter(and_(OrderContent.user_id == user_id, OrderContent.status == status)).all()
    
    def get_duplicate_in_cart(self, db: Session, user_id: UUID4, product_id: UUID4) -> Optional[OrderContent]:
        return db.query(OrderContent).join(Order).filter(and_(OrderContent.product_id == product_id, Order.status == OrderStatus.in_cart, Order.user_id == user_id)).first()

    def add_items(self, db: Session, obj_in: OrderContent, amount: int) -> OrderContent:
        obj_in.amount += amount
        db.commit()
        db.refresh(obj_in)
        return obj_in

    def update_status(self, db: Session, obj_in: OrderContent, ordercontent_status: OrderContentStatus) -> OrderContent:
        # Check if the status is a valid OrderContentStatus
        if not ordercontent_status in vars(OrderContentStatus).values():
            raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="The requested status does not exist",
            )
        obj_in.status = ordercontent_status
        db.commit()
        db.refresh(obj_in)
        return obj_in


ordercontent = CRUDOrderContent(OrderContent)