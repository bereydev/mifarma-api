from sqlalchemy.ext.hybrid import hybrid_property
from app.db.base_class import Base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

import uuid


class Product(Base):
    __tablename__ = 'products'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    ean_code = Column(String, nullable=False, index=True, unique=True)
    classification_number = Column(String)
    name = Column(String, nullable=False, index=True)
    description = Column(String)
    price = Column(Float, nullable=False, default=0)
    pharma_indications = Column(String)
    type_of_material = Column(Integer)
    magnitude = Column(Float)
    laboratory = Column(String)
    orders = relationship('Order', backref='product', lazy='dynamic', cascade="all,delete")
    stock_items = relationship('StockItem', backref='product', lazy='dynamic', cascade="all,delete")
    image = relationship('Image', backref='product', uselist=False)
    type = Column(String)

    @hybrid_property
    def image_filename(self):
        return self.image.filename

    __mapper_args__ = {
        'polymorphic_identity': 'products',
        'polymorphic_on': type
    }