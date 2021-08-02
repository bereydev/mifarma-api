from datetime import datetime
from typing import List, Optional

from pydantic.types import UUID4
from pydantic import BaseModel
from ..models.order import OrderStatus
from .product import Product



# Shared properties
class OrderBase(BaseModel):
    pharmacy_id: Optional[UUID4] = None
    user_id: Optional[ UUID4] = None
    product_id: Optional[UUID4] = None
    amount: int
    status: Optional[int] = OrderStatus.in_cart
    delivery_date: Optional[datetime]
    order_date: Optional[datetime]


# Properties to receive on order creation
class OrderCreate(OrderBase):
    pass


# Properties to receive on order update
class OrderUpdate(OrderBase):
    pass


# Properties shared by models stored in DB
class OrderInDBBase(OrderBase):
    id: UUID4
    user_id: UUID4
    product_id: UUID4
    pharmacy_id: UUID4
    product: Product

    class Config:
        orm_mode = True


# Properties to return to client
class Order(OrderInDBBase):
    pass


# Properties properties stored in DB
class OrderInDB(OrderInDBBase):
    pass
