from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, Date, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.ext.mutable import MutableDict

from app.db.base_class import Base
from .role import Role, RoleName
import uuid
from sqlalchemy.ext.hybrid import hybrid_property

if TYPE_CHECKING:
    from .drug import Drug  # noqa: F401

class Gender():
    male = 0
    female = 1
    non_binary = 2
    not_specified = 3

class User(Base):
    __tablename__='users'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    first_name = Column(String)
    last_name = Column(String)
    role_id = Column(UUID, ForeignKey('roles.id'))
    phone = Column(String)
    gender = Column(Integer, default=Gender.not_specified, nullable=False)
    pregnant = Column(Boolean(), default=False)
    birthdate = Column(Date)
    # Weight in kg
    weight = Column(Integer)
    # Height in mm
    height = Column(Integer)
    # List of Allergies with the following format "{<name of the allergie>:<true or false>,...}"
    allergies = Column(MutableDict.as_mutable(JSON), default={}, nullable=False)
    smoker = Column(Boolean(), default=False)
    addict = Column(Boolean(), default=False)
    alcoholic = Column(Boolean(), default=False) 
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    address = Column(String)
    postcode = Column(String)
    city = Column(String)
    country = Column(String)
    # List of current use of drugs and prescriptions of the following format "{'prescriptions':[<names>,...]}"
    prescriptions = Column(MutableDict.as_mutable(JSON), default={'prescriptions':[]}, nullable=False)
    # List of previous diseases with the following format "{<name of the diseases>:<true or false>,...}"
    previous_diseases = Column(MutableDict.as_mutable(JSON), default={}, nullable=False)
    # items = relationship("Item", back_populates="owner")
    pharmacy_id = Column(UUID, ForeignKey('pharmacies.id'))

    @hybrid_property
    def is_owner(self):
        return self.role.name == RoleName.OWNER
    @hybrid_property
    def is_admin(self):
        return self.role_id == RoleName.ADMIN
