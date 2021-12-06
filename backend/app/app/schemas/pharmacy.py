from typing import List, Optional

from pydantic import BaseModel
from pydantic.types import UUID4
from .user import User
from ..models.pharmacy import DEFAULT_SCHEDULE


# Shared properties
class PharmacyBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    address: Optional[str] = None
    address2: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    schedule: Optional[dict] = DEFAULT_SCHEDULE


# Properties to receive on pharmacy creation
class PharmacyCreate(PharmacyBase):
    name: str
    address: str
    address2: str
    country: str
    city: str
    schedule: dict = DEFAULT_SCHEDULE


# Properties to receive on pharmacy update
class PharmacyUpdate(PharmacyBase):
    pass


# Properties shared by models stored in DB
class PharmacyInDBBase(PharmacyBase):
    id: UUID4
    name: str
    address: str
    address2: str
    country: str
    city: str
    schedule: dict
    image_filename: Optional[str] = None

    class Config:
        orm_mode = True


# Properties to return to client
class Pharmacy(PharmacyInDBBase):
    pass


# Properties properties stored in DB
class PharmacyInDB(PharmacyInDBBase):
    pass
