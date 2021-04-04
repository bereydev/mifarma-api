from sqlalchemy.orm import session
from app.models.user import User
from .base import CRUDBase, CreateSchemaType, ModelType
from app.models import Pharmacy, pharmacy
from app.schemas import PharmacyCreate, PharmacyUpdate

class CRUDPharmacy(CRUDBase[Pharmacy, PharmacyCreate, PharmacyUpdate]):
    def create_with_owner(self, db: session, *, obj_in: CreateSchemaType, owner: User) -> ModelType:
        db_pharmacy = super().create(db, obj_in=obj_in)
        db_pharmacy.users.append(owner)
        db.commit()
        db.refresh(db_pharmacy)
        return db_pharmacy

pharmacy = CRUDPharmacy(Pharmacy)