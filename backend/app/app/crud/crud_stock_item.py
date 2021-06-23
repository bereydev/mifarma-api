from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException, status
from pydantic.types import UUID4
from sqlalchemy.orm import Session
from sqlalchemy import true, false
from .base import CRUDBase
from app.models import StockItem
from app.schemas import StockItemCreate, StockItemUpdate
from . import product, pharmacy

class CRUDStockItem(CRUDBase[StockItem, StockItemCreate, StockItemUpdate]):
    def create(self, db: Session, *, obj_in: StockItemCreate) -> StockItem:
        stock_item_data = jsonable_encoder(obj_in)
        product_obj = product.get(db, stock_item_data['product_id'])
        pharmacy_obj = pharmacy.get(db, stock_item_data['pharmacy_id'])

        if product_obj is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Drug with the given id does not exist"
            )

        if pharmacy_obj is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Pharmacy with the given id does not exist"
            )
        return super().create(db, obj_in=obj_in)

    # def create_with_product_and_pharmacy(self, db: Session, *, product_id: UUID4, pharmacy_id: UUID4, amount) -> StockItem:
    #     #TODO check if product already listed to avoid duplicate in the catalog
    #     db_obj = self.model(product_id=product_id, pharmacy_id=pharmacy_id)  # type: ignore
    #     db.add(db_obj)
    #     db.commit()
    #     db.refresh(db_obj)
    #     return db_obj


stock_item = CRUDStockItem(StockItem)