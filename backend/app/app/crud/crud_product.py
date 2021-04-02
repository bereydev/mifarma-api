from fastapi.encoders import jsonable_encoder
from pydantic.types import UUID4
from sqlalchemy.orm import Session
from .base import CRUDBase, CreateSchemaType
from app.models import Product
from app.schemas import ProductCreate, ProductUpdate
from pydantic.types import UUID4

class CRUDProduct(CRUDBase[Product, ProductCreate, ProductUpdate]):
     def create_with_pharmacy(self, db: Session, *, obj_in: CreateSchemaType, pharmacy_id: UUID4) -> Product:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, pharmacy_id=pharmacy_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


product = CRUDProduct(Product)