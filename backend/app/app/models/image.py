from sqlalchemy import Column, String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base
import uuid


class Image(Base):
    __tablename__ = 'images'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    product_id = Column(UUID(as_uuid=True), ForeignKey('products.id'))
    pharmacy_id = Column(UUID(as_uuid=True), ForeignKey('pharmacies.id'))

    @hybrid_property
    def filename(self):
        return self.name + "_" + str(self.id) + ".jpeg"