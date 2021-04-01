from typing import Optional

from .drug import Drug
from pydantic import BaseModel


# Shared properties
class ProductBase(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = 0
    discount: Optional[int] = 0


# Properties to receive on product creation
class ProductCreate(ProductBase):
    name: str


# Properties to receive on product update
class ProductUpdate(ProductBase):
    pass


# Properties shared by models stored in DB
class ProductInDBBase(ProductBase):
    id: int
    drug: Drug
    pharmacy_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Product(ProductInDBBase):
    pass


# Properties properties stored in DB
class ProductInDB(ProductInDBBase):
    pass
