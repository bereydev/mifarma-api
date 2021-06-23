from datetime import datetime
import uuid
from pydantic.errors import NumberNotGeError
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Integer
from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.db.base_class import Base

from datetime import datetime

if TYPE_CHECKING:
    from .ordercontent import OrderContent


class OrderStatus():
    in_cart = 0
    placed = 1
    closed = 2


class Order(Base):
    __tablename__ = 'orders'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    content = relationship('OrderContent', backref='order', cascade="all,delete")
    pharmacy_id = Column(UUID(as_uuid=True), ForeignKey('pharmacies.id'))
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    status = Column(Integer, nullable=False, default=OrderStatus.in_cart)
    order_date = Column(DateTime, nullable=False, default=datetime.utcnow())
