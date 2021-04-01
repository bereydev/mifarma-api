from typing import List, Optional
from .product import Product

from pydantic import BaseModel
from sqlalchemy.util.compat import inspect_getfullargspec


# Shared properties
class DrugBase(BaseModel):
    ean_code: Optional[str]
    name: Optional[str] = None
    description: Optional[str] = None
    pharma_indications: Optional[str] = None
    type_of_material: Optional[int] = None
    magnitude: Optional[float] = None
    laboratory: Optional[str] = None
    price: float



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
    id: int
    products: List[Product]

    class Config:
        orm_mode = True


# Properties to return to client
class Drug(DrugInDBBase):
    pass


# Properties properties stored in DB
class DrugInDB(DrugInDBBase):
    pass
