from sqlalchemy.ext.mutable import MutableDict
from app.schemas.user import UserInDB
from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Float, JSON
from sqlalchemy.orm import backref, relationship

from app.db.base_class import Base

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
    # pictures = 
    name = Column(String, index=True)
    address = Column(String)
    address2 = Column(String)
    country = Column(String)
    city = Column(String)
    employees = relationship('User', backref='pharmacy', foreign_keys='User.pharmacy_id')
    products = relationship('Product', backref='pharmacy')
    schedule = Column(MutableDict.as_mutable(JSON), default=DEFAULT_SCHEDULE, nullable=False)
    # Schedule an available hours
    # orders = 

