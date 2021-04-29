from typing import Optional

from pydantic import BaseModel, EmailStr
from pydantic.types import UUID4
from .role import Role
from datetime import date


# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    gender: Optional[int] = None
    pregnant: Optional[bool] = None
    birthdate: Optional[date] = None
    weight: Optional[int] = None
    height: Optional[int] = None
    allergies: Optional[dict] = None
    smoker: Optional[bool] = None
    alcoholic: Optional[bool] = None
    address: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    prescriptions: Optional[dict] = None
    previous_diseases: Optional[dict] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str


class OwnerCreate(UserCreate):
    pharmacist_number: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    pass


class UserInDBBase(UserBase):
    id: Optional[UUID4] = None
    role: Role
    confirmed: bool
    verified: bool
    activated: bool


    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
