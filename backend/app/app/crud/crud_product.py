from app.models.stock_item import StockItem
from typing import List
from fastapi.encoders import jsonable_encoder
from pydantic.types import UUID4
from sqlalchemy.orm import Session
from .base import CRUDBase, CreateSchemaType
from app.models import Product, Drug
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

     def get_multi_by_pharmacy(self, db: Session, *, skip: int, limit: int, filter: str, pharmacy_id: UUID4) -> List[Product]:
        products = (
            db.query(self.model)
            .join(StockItem)
            .filter(StockItem.pharmacy_id == pharmacy_id)
            .filter(StockItem.name_unaccented.ilike('%' + str(filter) + '%'))
            .offset(skip)
            .limit(limit)
            .all()
        )
        drugs = (
           db.query(Product)
           .filter(Product.type == 'drugs')
           .filter(Product.name_unaccented.ilike('%' + str(filter) + '%'))
           .offset(skip)
           .limit(limit)
           .all()
        )
        return (
           products.union(drugs)
        )


product = CRUDProduct(Product)