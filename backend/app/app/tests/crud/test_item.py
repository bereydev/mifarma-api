from sqlalchemy.orm import Session

from app import crud
from app.schemas.drug import DrugCreate, DrugUpdate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string


def test_create_drug(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    drug_in = DrugCreate(title=title, description=description)
    user = create_random_user(db)
    drug = crud.drug.create_with_owner(db=db, obj_in=drug_in, owner_id=user.id)
    assert drug.title == title
    assert drug.description == description
    assert drug.owner_id == user.id


def test_get_drug(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    drug_in = DrugCreate(title=title, description=description)
    user = create_random_user(db)
    drug = crud.drug.create_with_owner(db=db, obj_in=drug_in, owner_id=user.id)
    stored_drug = crud.drug.get(db=db, id=drug.id)
    assert stored_drug
    assert drug.id == stored_drug.id
    assert drug.title == stored_drug.title
    assert drug.description == stored_drug.description
    assert drug.owner_id == stored_drug.owner_id


def test_update_drug(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    drug_in = DrugCreate(title=title, description=description)
    user = create_random_user(db)
    drug = crud.drug.create_with_owner(db=db, obj_in=drug_in, owner_id=user.id)
    description2 = random_lower_string()
    drug_update = DrugUpdate(description=description2)
    drug2 = crud.drug.update(db=db, db_obj=drug, obj_in=drug_update)
    assert drug.id == drug2.id
    assert drug.title == drug2.title
    assert drug2.description == description2
    assert drug.owner_id == drug2.owner_id


def test_delete_drug(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    drug_in = DrugCreate(title=title, description=description)
    user = create_random_user(db)
    drug = crud.drug.create_with_owner(db=db, obj_in=drug_in, owner_id=user.id)
    drug2 = crud.drug.remove(db=db, id=drug.id)
    drug3 = crud.drug.get(db=db, id=drug.id)
    assert drug3 is None
    assert drug2.id == drug.id
    assert drug2.title == title
    assert drug2.description == description
    assert drug2.owner_id == user.id
