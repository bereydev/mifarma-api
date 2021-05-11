import uuid
from sqlalchemy.sql.sqltypes import DateTime

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from app.db.base_class import Base

class ProductStatus():
    in_cart = 0
    in_process = 1
    available = 2
    not_available = 3
    cancelled = 4 

class OrderContent(Base):
    __tablename__ = 'order_content'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    product_id = Column(UUID(as_uuid=True), ForeignKey('products.id'))
    order_id = Column(UUID(as_uuid=True), ForeignKey('orders.id'))
    amount = Column(Integer, nullable=False, default=1)
    status = Column(Integer, nullable=False, default=ProductStatus.in_cart)
    delivery_date = Column(DateTime)
    

