from datetime import datetime
from typing import Optional

from pydantic.types import UUID4
from pydantic import BaseModel
from .product import Product



# Shared properties
class ImageBase(BaseModel):
    pharmacy_id: Optional[UUID4] = None
    user_id: Optional[ UUID4] = None
    product_id: Optional[UUID4] = None
    name: Optional[str] = None
    


# Properties to receive on image creation
class ImageCreate(ImageBase):
    pass


# Properties to receive on image update
class ImageUpdate(ImageBase):
    pass


# Properties shared by models stored in DB
class ImageInDBBase(ImageBase):
    id: UUID4
    filename: str

    class Config:
        orm_mode = True


# Properties to return to client
class Image(ImageInDBBase):
    pass


# Properties properties stored in DB
class ImageInDB(ImageInDBBase):
    pass
