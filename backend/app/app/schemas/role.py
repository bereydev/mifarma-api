from typing import Optional, TYPE_CHECKING

from pydantic import BaseModel
from pydantic.types import UUID4

from .drug import Drug


# Shared properties
class RoleBase(BaseModel):
    name: Optional[str] = None
    premissions: Optional[int] = 0


# Properties to receive on role creation
class RoleCreate(RoleBase):
    name: str
    permissions: int


# Properties to receive on role update
class RoleUpdate(RoleBase):
    pass


# Properties shared by models stored in DB
class RoleInDBBase(RoleBase):
    id: UUID4

    class Config:
        orm_mode = True


# Properties to return to client
class Role(RoleInDBBase):
    pass


# Properties properties stored in DB
class RoleInDB(RoleInDBBase):
    pass
