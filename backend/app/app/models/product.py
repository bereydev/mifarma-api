from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base_class import Base
import uuid

class Product(Base):
    __tablename__ = 'products'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    ean_code = Column(String, nullable=False, index=True)
    classification_number = Column(String)
    name = Column(String, nullable=False, index=True)
    description = Column(String)
    price = Column(Float, nullable=False, default=0)
    pharma_indications = Column(String)
    type_of_material = Column(Integer)
    magnitude = Column(Float)
    laboratory = Column(String)
    order_content = relationship('OrderContent', backref='product')
    # pictures =
    type = Column(String)

    __mapper_args__ = {
        'polymorphic_identity': 'products',
        'polymorphic_on': type
    }
