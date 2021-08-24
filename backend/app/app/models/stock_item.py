from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import Integer, String, Float

from app.db.base_class import Base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
import unidecode
import uuid 


class StockItem(Base):
    __tablename__ = 'stock_items'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    pharmacy_id = Column(UUID(as_uuid=True), ForeignKey('pharmacies.id'), nullable=False)
    amount = Column(Integer, default=0, nullable=False)
    product_id = Column(UUID(as_uuid=True), ForeignKey('products.id'), nullable=False)
    # name discount and price allow to override or add new values 
    # in a pharmacy catalog
    name = Column(String)
    name_unaccented = Column(String, index=True)
    discount = Column(Integer, default=0, nullable=False)
    price = Column(Float, default=0, nullable=False)

    @hybrid_property
    def is_available(self):
        return self.amount > 0

    @validates('name')
    def update_name_unaccented(self, key, name):
        self.name_unaccented = unidecode.unidecode(name)
        return name