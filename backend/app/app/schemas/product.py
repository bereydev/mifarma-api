from typing import Optional

from pydantic import BaseModel


# Shared properties
class ProductBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on drug creation
class ProductCreate(ProductBase):
    title: str


# Properties to receive on drug update
class ProductUpdate(ProductBase):
    pass


# Properties shared by models stored in DB
class ProductInDBBase(ProductBase):
    id: int
    title: str
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Product(ProductInDBBase):
    pass


# Properties properties stored in DB
class ProductInDB(ProductInDBBase):
    pass
