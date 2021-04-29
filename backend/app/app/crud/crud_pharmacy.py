from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import false, true
from .base import CRUDBase
from app.models import Pharmacy
from app.schemas import PharmacyCreate, PharmacyUpdate
from fastapi.encoders import jsonable_encoder

class CRUDPharmacy(CRUDBase[Pharmacy, PharmacyCreate, PharmacyUpdate]):
    def get_multi_active(self, db: Session, *, skip: int, limit: int) -> List[Pharmacy]:
        return db.query(Pharmacy).offset(skip).limit(limit).all()
    
    def get_multi_inactive(self, db: Session, *, skip: int, limit: int) -> List[Pharmacy]:
        return db.query(Pharmacy).offset(skip).limit(limit).all()


pharmacy = CRUDPharmacy(Pharmacy)