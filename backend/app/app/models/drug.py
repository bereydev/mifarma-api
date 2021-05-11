from app.models import stock_item
from typing import TYPE_CHECKING

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from sqlalchemy.sql.schema import ForeignKey

from .product import Product

if TYPE_CHECKING:
    from .stock_item import StockItem # noqa: F401


class Drug(Product):
    __tablename__ = 'drugs'
    id = Column(UUID(as_uuid=True), ForeignKey('products.id'), primary_key=True, index=True)
    stock_items = relationship('StockItem', backref='drug', lazy='dynamic', cascade="all,delete", foreign_keys='StockItem.drug_id')

    __mapper_args__ = {
        'polymorphic_identity': 'drugs'
    }

