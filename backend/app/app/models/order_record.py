from datetime import datetime
import uuid
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.operators import as_
from sqlalchemy.sql.schema import PrimaryKeyConstraint
from sqlalchemy.sql.sqltypes import Date, DateTime
from app.models.abstract_product import AbstractProduct
from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from app.db.base_class import Base

from .abstract_product import AbstractProduct
from datetime import datetime
if TYPE_CHECKING:
    from .drug import Drug  # noqa: F401
    from .pharmacy import Pharmacy #noqa: F401 

class OrderStatus():
    in_cart = 0
    in_process = 1
    available = 2
    not_available = 3
    cancelled = 4 

class OrderRecord(Base):
    __tablename__ = 'order_records'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    product_id = Column(UUID(as_uuid=True), ForeignKey('products.id'))
    pharmacy_id = Column(UUID(as_uuid=True), ForeignKey('pharmacies.id'))
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    status = Column(Integer, nullable=False, default=OrderStatus.in_cart)
    order_date = Column(DateTime, nullable=False, default=datetime.utcnow())
    delivery_date = Column(DateTime)
    

