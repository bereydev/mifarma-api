from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null

from app.db.base_class import Base

if TYPE_CHECKING:
    from .product import Product # noqa: F401


class Drug(Base):
    __tablename__ = 'drugs'
    id = Column(Integer, primary_key=True, index=True)
    ean_code = Column(String, nullable=False, index=True)
    name = Column(String, nullable=False, index=True)
    description = Column(String)
    pharma_indications = Column(String)
    type_of_material = Column(Integer)
    magnitude = Column(Float)
    laboratory = Column(String)
    price = Column(Float, nullable=False)
    # pictures =
    products = relationship('Product', backref='drug', lazy='dynamic')

