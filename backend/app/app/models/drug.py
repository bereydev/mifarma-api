from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .product import Product # noqa: F401


class Drug(Base):
    __tablename__ = 'drugs'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type_of_material = Column(Integer)
    price = Column(Float, nullable=False)
    magnitude = Column(Float)
    # description = (leaflet, AEMPS, Aplicacion CIMA)
    # pictures =
    laboratory = Column(String)
    # legal_type =
    # indicationes Farmatic
    products = relationship('Product', backref='drug', lazy='dynamic')

