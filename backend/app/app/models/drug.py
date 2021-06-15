from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean

from .product import Product


class Drug(Product):
    __tablename__ = 'drugs'
    id = Column(UUID(as_uuid=True), ForeignKey('products.id'), primary_key=True, index=True)
    with_prescription = Column(Boolean, default=False, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'drugs'
    }

