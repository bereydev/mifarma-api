from typing import Optional
from pydantic.types import UUID4

from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.drug import DrugCreate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string


def create_random_drug(db: Session, *, owner_id: Optional[UUID4] = None) -> models.Drug:
    if owner_id is None:
        user = create_random_user(db)
        owner_id = user.id
    title = random_lower_string()
    description = random_lower_string()
    drug_in = DrugCreate(title=title, description=description, id=id)
    return crud.drug.create_with_owner(db=db, obj_in=drug_in, owner_id=owner_id)
