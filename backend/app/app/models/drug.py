from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


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
    products = relationship('Product', backref='reference', lazy='dynamic')


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    discount = Column(Integer, default=0)
    reference_id = Column(Integer, ForeignKey('drugs.id'))

    @classmethod
    def create_product(cls, drug: Drug, name: str, price: float, discount: int = 0):
        name = drug.name if name is None else name
        price = drug.price if price is None else price
        return cls(name=name,
                   price=price,
                   discount=discount)
