import uuid

from sqlalchemy import Column, ForeignKey, Integer, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.expression import null
from app.db.base_class import Base
from datetime import datetime

class OrderStatus():
    in_cart = 0
    placed = 1
    available = 2
    not_available = 3
    delivered = 4

class Order(Base):
    __tablename__ = 'orders'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    product_id = Column(UUID(as_uuid=True), ForeignKey('products.id'))
    amount = Column(Integer, nullable=False, default=1)
    status = Column(Integer, nullable=False, default=OrderStatus.in_cart)
    pharmacy_id = Column(UUID(as_uuid=True), ForeignKey('pharmacies.id'))
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    order_date = Column(DateTime, nullable=False, default=datetime.utcnow())
    delivery_date = Column(DateTime)
    count_for_voucher = Column(Boolean, nullable=False, default=False)
    

