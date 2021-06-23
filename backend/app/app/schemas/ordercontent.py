from datetime import datetime
from typing import List, Optional

from pydantic.types import UUID4
from pydantic import BaseModel
from ..models.ordercontent import OrderContentStatus
from .product import Product



# Shared properties
class OrderContentBase(BaseModel):
    product_id: UUID4
    order_id: UUID4
    amount: int
    status: Optional[int] = OrderContentStatus.in_cart
    delivery_date: Optional[datetime]


# Properties to receive on order creation
class OrderContentCreate(OrderContentBase):
    pass


# Properties to receive on order update
class OrderContentUpdate(OrderContentBase):
    pass


# Properties shared by models stored in DB
class OrderContentInDBBase(OrderContentBase):
    id: UUID4
    product: Product

    class Config:
        orm_mode = True


# Properties to return to client
class OrderContent(OrderContentInDBBase):
    pass


# Properties properties stored in DB
class OrderContentInDB(OrderContentInDBBase):
    pass
