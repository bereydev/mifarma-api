from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base
import uuid


class Image(Base):
    __tablename__ = 'images'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String)
    filename = Column(String)