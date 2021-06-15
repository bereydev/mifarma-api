from typing import Optional

from pydantic.types import UUID4
from .product import ProductBase


# Shared properties
class DrugBase(ProductBase):
    with_prescription: Optional[bool] = False



# Properties to receive on drug creation
class DrugCreate(DrugBase):
    ean_code: str
    name: str
    price: int


# Properties to receive on drug update
class DrugUpdate(DrugBase):
    pass


# Properties shared by models stored in DB
class DrugInDBBase(DrugBase):
    id: UUID4

    class Config:
        orm_mode = True


# Properties to return to client
class Drug(DrugInDBBase):
    pass


# Properties properties stored in DB
class DrugInDB(DrugInDBBase):
    pass
