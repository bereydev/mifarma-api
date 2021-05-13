from typing import Optional

from pydantic import BaseModel, EmailStr
from pydantic.types import UUID4
from .role import Role
from datetime import date


# Shared properties
class OwnerBase(BaseModel):
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    gender: Optional[int] = None
    birthdate: Optional[date] = None


# Properties to receive via API on creation
class OwnerCreate(OwnerBase):
    email: EmailStr
    phone: str
    pharmacist_number: str
    password: str


# Properties to receive via API on update
class OwnerUpdate(OwnerBase):
    pass


class OwnerInDBBase(OwnerBase):
    id: Optional[UUID4] = None
    role: Role
    confirmed: bool
    verified: bool
    activated: bool


    class Config:
        orm_mode = True


# Additional properties to return via API
class Owner(OwnerInDBBase):
    pass


# Additional properties stored in DB
class OwnerInDB(OwnerInDBBase):
    hashed_password: str
