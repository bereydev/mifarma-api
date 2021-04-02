from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from pydantic.types import UUID4
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Drug])
def read_drugs(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve drugs.
    """
    if crud.user.is_admin(current_user):
        drugs = crud.drug.get_multi(db, skip=skip, limit=limit)
    else:
        drugs = crud.drug.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return drugs


@router.post("/", response_model=schemas.Drug)
def create_drug(
    *,
    db: Session = Depends(deps.get_db),
    drug_in: schemas.DrugCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new drug.
    """
    drug = crud.drug.create_with_owner(db=db, obj_in=drug_in, owner_id=current_user.id)
    return drug


@router.put("/{id}", response_model=schemas.Drug)
def update_drug(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID4,
    drug_in: schemas.DrugUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an drug.
    """
    drug = crud.drug.get(db=db, id=id)
    if not drug:
        raise HTTPException(status_code=404, detail="Drug not found")
    if not crud.user.is_admin(current_user) and (drug.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    drug = crud.drug.update(db=db, db_obj=drug, obj_in=drug_in)
    return drug


@router.get("/{id}", response_model=schemas.Drug)
def read_drug(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID4,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get drug by ID.
    """
    drug = crud.drug.get(db=db, id=id)
    if not drug:
        raise HTTPException(status_code=404, detail="Drug not found")
    if not crud.user.is_admin(current_user) and (drug.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return drug


@router.delete("/{id}", response_model=schemas.Drug)
def delete_drug(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID4,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an drug.
    """
    drug = crud.drug.get(db=db, id=id)
    if not drug:
        raise HTTPException(status_code=404, detail="Drug not found")
    if not crud.user.is_admin(current_user) and (drug.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    drug = crud.drug.remove(db=db, id=id)
    return drug
