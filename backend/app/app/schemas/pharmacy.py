from typing import Optional

from pydantic import BaseModel


# Shared properties
class PharmacyBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on drug creation
class PharmacyCreate(PharmacyBase):
    title: str


# Properties to receive on drug update
class PharmacyUpdate(PharmacyBase):
    pass


# Properties shared by models stored in DB
class PharmacyInDBBase(PharmacyBase):
    id: int
    title: str
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Pharmacy(PharmacyInDBBase):
    pass


# Properties properties stored in DB
class PharmacyInDB(PharmacyInDBBase):
    pass
