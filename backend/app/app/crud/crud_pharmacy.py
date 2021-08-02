from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import true, false, or_, and_
from .base import CRUDBase
from app.models import Pharmacy, User, Role
from app.models.role import RoleName
from app.schemas import PharmacyCreate, PharmacyUpdate

class CRUDPharmacy(CRUDBase[Pharmacy, PharmacyCreate, PharmacyUpdate]):
    def get_multi_active(self, db: Session, *, skip: int, limit: int, filter: str) -> List[Pharmacy]:
        return (
            db.query(Pharmacy)
            .filter(or_(Pharmacy.name.ilike('%' + str(filter) + '%'), Pharmacy.city.ilike('%' + str(filter) + '%'), Pharmacy.address.ilike('%' + str(filter) + '%'), Pharmacy.address2.ilike('%' + str(filter) + '%')))
            .join(User)
            .filter(and_(User.confirmed == true(), User.verified == true(), User.activated == true()))
            .join(Role)
            .filter(Role.name == RoleName.OWNER)
            .offset(skip)
            .limit(limit)
            .all()
            )
    
    def get_multi_inactive(self, db: Session, *, skip: int, limit: int) -> List[Pharmacy]:
        return (
            db.query(Pharmacy)
            .join(User)
            .filter(or_(User.confirmed == false(), User.verified == false(), User.activated == false()))
            .join(Role)
            .filter(Role.name == RoleName.OWNER)
            .offset(skip)
            .limit(limit)
            .all()
            )


pharmacy = CRUDPharmacy(Pharmacy)