from typing import Optional

from pydantic import BaseModel


# Shared properties
class DrugBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on drug creation
class DrugCreate(DrugBase):
    title: str


# Properties to receive on drug update
class DrugUpdate(DrugBase):
    pass


# Properties shared by models stored in DB
class DrugInDBBase(DrugBase):
    id: int
    title: str
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Drug(DrugInDBBase):
    pass


# Properties properties stored in DB
class DrugInDB(DrugInDBBase):
    pass
