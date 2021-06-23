from app.models import pharmacy, stock_item
from typing import List, Optional
from pydantic.main import BaseModel

from pydantic.types import UUID4
from .product import Product


# Shared properties
class StockItemBase(BaseModel):
    amount: Optional[int] = 0
    name: Optional[str]
    discount: Optional[float] = 0
    price: Optional[int] = 0
    product_id: UUID4
    pharmacy_id: UUID4


# Properties to receive on stock_item creation
class StockItemCreate(StockItemBase):
    pass

# Properties to receive on stock_item update
class StockItemUpdate(StockItemBase):
    pass


# Properties shared by models stored in DB
class StockItemInDBBase(StockItemBase):
    id: UUID4
    product: Product

    class Config:
        orm_mode = True


# Properties to return to client
class StockItem(StockItemInDBBase):
    pass


# Properties properties stored in DB
class StockItemInDB(StockItemInDBBase):
    pass
