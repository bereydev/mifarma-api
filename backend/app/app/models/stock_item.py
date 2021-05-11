from app.models.product import Product
from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID

from .product import Product

if TYPE_CHECKING:
    from .drug import Drug  # noqa: F401
    from .pharmacy import Pharmacy #noqa: F401 
    from .order import OrderContent #noqa: F401

class StockItem(Product):
    __tablename__ = 'stock_items'
    id = Column(UUID(as_uuid=True), ForeignKey('products.id'), primary_key=True, index=True)
    pharmacy_id = Column(UUID(as_uuid=True), ForeignKey('pharmacies.id'))
    drug_id = Column(UUID(as_uuid=True), ForeignKey('drugs.id'))
    discount = Column(Integer, default=0)

    __mapper_args__ = {
        'polymorphic_identity': 'stock_items'
    }