from sqlalchemy.orm import relationship
from app.models.order_record import OrderRecord
from app.models.abstract_product import AbstractProduct
from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from .abstract_product import AbstractProduct

if TYPE_CHECKING:
    from .drug import Drug  # noqa: F401
    from .pharmacy import Pharmacy #noqa: F401 

class Product(AbstractProduct):
    __tablename__ = 'products'
    id = Column(UUID(as_uuid=True), ForeignKey('abstract_products.id'), primary_key=True, index=True)
    pharmacy_id = Column(UUID(as_uuid=True), ForeignKey('pharmacies.id'))
    drug_id = Column(UUID(as_uuid=True), ForeignKey('drugs.id')) 
    order_record = relationship('OrderRecord', backref='product', uselist=False)

    __mapper_args__ = {
        'polymorphic_identity': 'products'
    }


    @classmethod
    def create_product(cls, drug: 'Drug', pharmacy: 'Pharmacy', name: str, price: float, discount: int = 0):
        name = drug.name if name is None else name
        price = drug.price if price is None else price
        return cls(name=name,
                   price=price,
                   discount=discount,
                   drug_id=drug.id,
                   pharmacy_id=pharmacy.id)