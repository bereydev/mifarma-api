from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base
import uuid

class AbstractProduct(Base):
    __tablename__ = 'abstract_products'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    ean_code = Column(String, nullable=False, index=True)
    name = Column(String, nullable=False, index=True)
    description = Column(String)
    price = Column(Float, nullable=False, default=0)
    discount = Column(Integer, default=0)
    pharma_indications = Column(String)
    type_of_material = Column(Integer)
    magnitude = Column(Float)
    laboratory = Column(String)
    pharmacy_id = Column(UUID(as_uuid=True), ForeignKey('pharmacies.id'))
    # pictures =
    type = Column(String)

    __mapper_args__ = {
        'polymorphic_identity': 'abstract_products',
        'polymorphic_on': type
    }
