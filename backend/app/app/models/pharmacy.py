from sqlalchemy.ext.mutable import MutableDict
from typing import TYPE_CHECKING

from sqlalchemy import Column, String, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from .role import Role, RoleName
import uuid

if TYPE_CHECKING:
    from .user import User  # noqa: F401
    from .order import Order #noqa: F401

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
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String)
    address = Column(String)
    address2 = Column(String)
    country = Column(String)
    city = Column(String)
    users = relationship('User', backref='pharmacy', lazy='dynamic')
    stock_items = relationship('StockItem', backref='pharmacy', cascade="all,delete", lazy='dynamic')
    orders = relationship('Order', backref='pharmacy', cascade="all,delete", lazy='dynamic')
    schedule = Column(MutableDict.as_mutable(JSON), default=DEFAULT_SCHEDULE, nullable=False)
    # pictures = 

    def get_owner(self):
        return self.users.join(Role).filter(Role.name == RoleName.OWNER).first()
    
    def get_employees(self):
        return self.users.join(Role).filter(Role.name == RoleName.EMPLOYEE)

    def get_customers(self):
        return self.users.join(Role).filter(Role.name == RoleName.CUSTOMER)

