from app.models.user import Gender
from typing import Optional

from pydantic import BaseModel, EmailStr
from pydantic.types import UUID4
from .role import Role
from datetime import date


# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    first_name: Optional[str] = 'John'
    last_name: Optional[str] = 'Doe'
    public_id: Optional[str]
    phone: Optional[str] = '+34700000000'
    gender: Optional[int] = Gender.not_specified
    pregnant: Optional[bool] = None
    birthdate: Optional[date] = None
    weight: Optional[int] = None
    height: Optional[int] = None
    allergies: Optional[dict] = {'list':[]}
    smoker: Optional[bool] = None
    addict: Optional[bool] = None
    alcoholic: Optional[bool] = None
    address: Optional[str] = None
    postcode: Optional[str] = '18000'
    city: Optional[str] = 'Granada'
    country: Optional[str] = 'Spain'
    prescriptions: Optional[dict] = {'list':[]}
    previous_diseases: Optional[dict] = {'list':[]}


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str = 'Password1234'


# Properties to receive via API on update
class UserUpdate(UserBase):
    pass


class UserInDBBase(UserBase):
    id: Optional[UUID4] = None
    public_id: str
    role: Role
    confirmed: bool
    verified: bool
    activated: bool
    voucher: float


    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
