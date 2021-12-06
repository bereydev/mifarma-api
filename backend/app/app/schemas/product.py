from typing import Optional

from pydantic import BaseModel
from pydantic.types import UUID4


# Shared properties
class ProductBase(BaseModel):
    ean_code: Optional[str] = None
    classification_number: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = 0
    pharma_indications: Optional[str] = None
    type_of_material: Optional[int] = None
    magnitude: Optional[float] = None
    laboratory: Optional[str] = None

# Properties to receive on product creation
class ProductCreate(ProductBase):
    name: str


# Properties to receive on product update
class ProductUpdate(ProductBase):
    pass


# Properties shared by models stored in DB
class ProductInDBBase(ProductBase):
    id: UUID4
    type: str
    image_filename: Optional[str] = None

    class Config:
        orm_mode = True


# Properties to return to client
class Product(ProductInDBBase):
    pass


# Properties properties stored in DB
class ProductInDB(ProductInDBBase):
    pass
