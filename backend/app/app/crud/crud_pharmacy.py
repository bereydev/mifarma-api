from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import true, false
from .base import CRUDBase
from app.models import Pharmacy, User
from app.schemas import PharmacyCreate, PharmacyUpdate

class CRUDPharmacy(CRUDBase[Pharmacy, PharmacyCreate, PharmacyUpdate]):
    def get_multi_active(self, db: Session, *, skip: int, limit: int) -> List[Pharmacy]:
        return db.query(Pharmacy).join(User).filter(User.activated == true()).offset(skip).limit(limit).all()
    
    def get_multi_inactive(self, db: Session, *, skip: int, limit: int) -> List[Pharmacy]:
        return db.query(Pharmacy).join(User).filter(User.activated == false()).offset(skip).limit(limit).all()


pharmacy = CRUDPharmacy(Pharmacy)