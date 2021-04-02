from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from pydantic.types import UUID4
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Pharmacy])
def read_pharmacys(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve pharmacies.
    """
    if crud.user.is_admin(current_user):
        pharmacies = crud.pharmacy.get_multi(db, skip=skip, limit=limit)
    else:
        pharmacies = crud.pharmacy.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return pharmacies


@router.post("/", response_model=schemas.Pharmacy)
def create_pharmacy(
    *,
    db: Session = Depends(deps.get_db),
    pharmacy_in: schemas.PharmacyCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new pharmacy.
    """
    pharmacy = crud.pharmacy.create_with_owner(db=db, obj_in=pharmacy_in, owner_id=current_user.id)
    return pharmacy


@router.put("/{id}", response_model=schemas.Pharmacy)
def update_pharmacy(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID4,
    pharmacy_in: schemas.PharmacyUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an pharmacy.
    """
    pharmacy = crud.pharmacy.get(db=db, id=id)
    if not pharmacy:
        raise HTTPException(status_code=404, detail="Pharmacy not found")
    if not crud.user.is_admin(current_user) and (pharmacy.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    pharmacy = crud.pharmacy.update(db=db, db_obj=pharmacy, obj_in=pharmacy_in)
    return pharmacy


@router.get("/{id}", response_model=schemas.Pharmacy)
def read_pharmacy(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID4,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get pharmacy by ID.
    """
    pharmacy = crud.pharmacy.get(db=db, id=id)
    if not pharmacy:
        raise HTTPException(status_code=404, detail="Pharmacy not found")
    if not crud.user.is_admin(current_user) and (pharmacy.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return pharmacy


@router.delete("/{id}", response_model=schemas.Pharmacy)
def delete_pharmacy(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID4,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an pharmacy.
    """
    pharmacy = crud.pharmacy.get(db=db, id=id)
    if not pharmacy:
        raise HTTPException(status_code=404, detail="Pharmacy not found")
    if not crud.user.is_admin(current_user) and (pharmacy.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    pharmacy = crud.pharmacy.remove(db=db, id=id)
    return pharmacy
