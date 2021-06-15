from typing import List
from fastapi.encoders import jsonable_encoder
from pydantic.types import UUID4
from sqlalchemy.orm import Session
from sqlalchemy import true, false
from .base import CRUDBase
from app.models import StockItem
from app.schemas import StockItemCreate, StockItemUpdate

class CRUDStockItem(CRUDBase[StockItem, StockItemCreate, StockItemUpdate]):
    def create_with_product_and_pharmacy(self, db: Session, *, product_id: UUID4, pharmacy_id: UUID4) -> StockItem:
        #TODO check if product already listed to avoid duplicate in the catalog
        db_obj = self.model(product_id=product_id, pharmacy_id=pharmacy_id)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


stock_item = CRUDStockItem(StockItem)