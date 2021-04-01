from sqlalchemy.ext.mutable import MutableDict
from app.schemas.user import UserInDB
from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Float, JSON
from sqlalchemy.orm import backref, relationship

from app.db.base_class import Base
from .role import Role, RoleName

if TYPE_CHECKING:
    from .user import User  # noqa: F401
    from .drug import Product # noqa: F401

DEFAULT_SCHEDULE = {
    'monday':0,
    'tuesday':0,
    'wednesday':0,
    'thursday':0,
    'friday':0,
    'saturday':0,
    'sunday':0
}

class Pharmacy(Base):
    __tablename__='pharmacies'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String)
    address = Column(String)
    address2 = Column(String)
    country = Column(String)
    city = Column(String)
    users = relationship('User', backref='pharmacy', lazy='dynamic')
    products = relationship('Product', backref='pharmacy', lazy='dynamic')
    schedule = Column(MutableDict.as_mutable(JSON), default=DEFAULT_SCHEDULE, nullable=False)
    # orders = 
    # pictures = 

    def get_owner(self):
        return self.users.join(Role).filter(Role.name == RoleName.OWNER).first()

    def get_employees(self):
        return self.users.join(Role).filter(Role.name == RoleName.EMPLOYEE)

    def get_customers(self):
        return self.users.join(Role).filter(Role.name == RoleName.CUSTOMER)

