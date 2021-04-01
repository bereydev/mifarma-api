from app.crud.base import CRUDBase
from app.models import Drug
from app.schemas import DrugCreate, DrugUpdate

drug = CRUDBase[Drug, DrugCreate, DrugUpdate](Drug)