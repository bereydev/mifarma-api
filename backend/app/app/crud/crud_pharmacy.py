from .base import CRUDBase
from app.models import Pharmacy, pharmacy
from app.schemas import PharmacyCreate, PharmacyUpdate

pharmacy = CRUDBase[Pharmacy, PharmacyCreate, PharmacyUpdate](Pharmacy)