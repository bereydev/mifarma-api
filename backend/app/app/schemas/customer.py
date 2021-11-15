from typing import Optional
from app.schemas import pharmacy

from pydantic import BaseModel, EmailStr
from pydantic.types import UUID4
from .role import Role
from datetime import date


# Shared properties
class CustomerBase(BaseModel):
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
    postcode: Optional[str] = None
    prescriptions: Optional[dict] = None
    previous_diseases: Optional[dict] = None


# Properties to receive via API on creation
class CustomerCreate(CustomerBase):
    # Phone or email is mandatory
    password: str


# Properties to receive via API on update
class CustomerUpdate(CustomerBase):
    pass


class CustomerInDBBase(CustomerBase):
    id: UUID4
    pharmacy_id: Optional[UUID4] = None
    role: Role
    confirmed: bool
    verified: bool
    activated: bool
    voucher: Optional[float] = 0


    class Config:
        orm_mode = True


# Additional properties to return via API
class Customer(CustomerInDBBase):
    pass


# Additional properties stored in DB
class CustomerInDB(CustomerInDBBase):
    hashed_password: str
