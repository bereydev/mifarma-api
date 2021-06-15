from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic.types import UUID4
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


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
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Drug not found")
    return drug


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
    drugs = crud.drug.get_multi(db, skip=skip, limit=limit)
    return drugs
