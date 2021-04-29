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
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Retrieve drugs.
    """
    if current_user.is_admin:
        drugs = crud.drug.get_multi(db, skip=skip, limit=limit)
    return drugs


@router.get("/{id}", response_model=schemas.Drug)
def read_drug(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID4,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Get drug by ID.
    """
    drug = crud.drug.get(db=db, id=id)
    if not drug:
        raise HTTPException(status_code=404, detail="Drug not found")
    if not current_user.is_admin:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return drug


@router.post("/")
def update_catalog(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Update the drug catalog from a CSV/EXCEL file
    """
    if not current_user.is_admin:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    # TODO parse the document
    return {'success': True, 'msg': 'The catalog is successfully updated'}


