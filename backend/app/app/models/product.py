from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base
import uuid

if TYPE_CHECKING:
    from .drug import Drug  # noqa: F401
    from .pharmacy import Pharmacy #noqa: F401

class Product(Base):
    __tablename__ = 'products'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, nullable=False, index=True)
    price = Column(Float, nullable=False, default=0)
    discount = Column(Integer, default=0)
    drug_id = Column(UUID, ForeignKey('drugs.id'))
    pharmacy_id = Column(UUID, ForeignKey('pharmacies.id'))

    @classmethod
    def create_product(cls, drug: 'Drug', pharmacy: 'Pharmacy', name: str, price: float, discount: int = 0):
        name = drug.name if name is None else name
        price = drug.price if price is None else price
        return cls(name=name,
                   price=price,
                   discount=discount,
                   drug_id=drug.id,
                   pharmacy_id=pharmacy.id)