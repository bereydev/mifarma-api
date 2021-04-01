from typing import List, Optional, 

from pydantic import BaseModel
from .user import User


# Shared properties
class PharmacyBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    address: Optional[str] = None
    address2: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    schedule: Optional[str] = None


# Properties to receive on pharmacy creation
class PharmacyCreate(PharmacyBase):
    name: str
    address: str
    address2: str
    country: str
    city: str
    schedule: str


# Properties to receive on pharmacy update
class PharmacyUpdate(PharmacyBase):
    pass


# Properties shared by models stored in DB
class PharmacyInDBBase(PharmacyBase):
    id: int
    title: str
    owner: User
    customers: List[User]
    employees: List[User]

    class Config:
        orm_mode = True


# Properties to return to client
class Pharmacy(PharmacyInDBBase):
    pass


# Properties properties stored in DB
class PharmacyInDB(PharmacyInDBBase):
    pass
