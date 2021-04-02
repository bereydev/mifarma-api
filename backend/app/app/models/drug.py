from app.models.abstract_product import AbstractProduct
from typing import TYPE_CHECKING

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from sqlalchemy.sql.schema import ForeignKey

from .abstract_product import AbstractProduct

if TYPE_CHECKING:
    from .product import Product # noqa: F401


class Drug(AbstractProduct):
    __tablename__ = 'drugs'
    id = Column(UUID(as_uuid=True), ForeignKey('abstract_products.id'), primary_key=True, index=True)
    products = relationship('Product', backref='drug', lazy='dynamic', foreign_keys='Product.drug_id')

    __mapper_args__ = {
        'polymorphic_identity': 'drugs'
    }

