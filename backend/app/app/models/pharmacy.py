from app.schemas import pharmacy
from sqlalchemy.ext.mutable import MutableDict
from app.schemas.user import UserInDB
from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Float, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import backref, relationship

from app.db.base_class import Base
from .role import Role, RoleName
from .drug import Drug
from .product import Product
import uuid

if TYPE_CHECKING:
    from .user import User  # noqa: F401
    from .drug import Product # noqa: F401
    from .abstract_product import AbstractProduct # noqa: F401

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
    abstract_products = relationship('AbstractProduct', backref='pharmacy', lazy='dynamic')
    schedule = Column(MutableDict.as_mutable(JSON), default=DEFAULT_SCHEDULE, nullable=False)
    # orders = 
    # pictures = 

    def get_owner(self):
        return self.users.join(Role).filter(Role.name == RoleName.OWNER).first()

    def get_employees(self):
        return self.users.join(Role).filter(Role.name == RoleName.EMPLOYEE)

    def get_customers(self):
        return self.users.join(Role).filter(Role.name == RoleName.CUSTOMER)

    def get_catalog(self):
        return self.abstract_products.filter(AbstractProduct.type == 'products').union(Drug.query.all().join(Product).filter(Product.pharmacy_id == self.id))
