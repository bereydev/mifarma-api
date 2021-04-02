from typing import Optional, TYPE_CHECKING

from pydantic import BaseModel
from pydantic.types import UUID4

from .drug import Drug


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
    id: UUID4
    drug: Drug
    pharmacy_id: UUID4

    class Config:
        orm_mode = True


# Properties to return to client
class Product(ProductInDBBase):
    pass


# Properties properties stored in DB
class ProductInDB(ProductInDBBase):
    pass
