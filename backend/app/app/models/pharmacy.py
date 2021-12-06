from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.mutable import MutableDict
from typing import TYPE_CHECKING

from sqlalchemy import Column, String, JSON, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from .role import Role, RoleName
import uuid

if TYPE_CHECKING:
    from .user import User  # noqa: F401
    from .stock_item import StockItem # noqa: F401
    from .image import Image # noqa: F401

DEFAULT_SCHEDULE = {
    "Lunes": [
        "09:00-14:30",
        "17:30-21:00"
    ],
    "Martes": [
        "09:00-14:30",
        "17:30-21:00"
    ],
    "Miercoles": [
        "09:00-14:30",
        "17:30-21:00"
    ],
    "Jueves": [
        "09:00-14:30",
        "17:30-21:00"
    ],
    "Viernes": [
        "09:00-14:30",
        "17:30-21:00"
    ],
    "Sabado": [
        "09:00-14:30",
        "17:30-21:00"
    ],
    "Domingo": [
        "09:00-14:30",
        "17:30-21:00"
    ]
}


class Pharmacy(Base):
    __tablename__ = 'pharmacies'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String)
    address = Column(String)
    address2 = Column(String)
    country = Column(String)
    city = Column(String)
    users = relationship('User', backref='pharmacy', lazy='dynamic')
    stock_items = relationship('StockItem', backref='pharmacy',
                               cascade="all,delete", lazy='dynamic')
    orders = relationship('Order', backref='pharmacy',
                          cascade="all,delete", lazy='dynamic')
    schedule = Column(MutableDict.as_mutable(
        JSON), default=DEFAULT_SCHEDULE, nullable=False)
    email = Column(String)
    phone = Column(String)
    percentage_for_voucher = Column(Integer, nullable=False, default=0)
    image = relationship('Image', backref='pharmacy', uselist=False)

    @hybrid_property
    def image_filename(self):
        return self.image.filename

    def get_owner(self):
        return self.users.join(Role).filter(Role.name == RoleName.OWNER).first()

    def get_employees(self):
        return self.users.join(Role).filter(Role.name == RoleName.EMPLOYEE)

    def get_customers(self):
        return self.users.join(Role).filter(Role.name == RoleName.CUSTOMER)

