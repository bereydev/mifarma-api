from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic.types import UUID4
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/active", response_model=List[schemas.Pharmacy])
def read_active_pharmacys(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve active pharmacies.
    """
    pharmacies = crud.pharmacy.get_multi_active(db, skip=skip, limit=limit)
    return pharmacies


@router.get("/inactive", response_model=List[schemas.Pharmacy])
def read_inactive_pharmacys(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Retrieve active pharmacies.
    """
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user doesn't have enough privileges"
        )
    pharmacies = crud.pharmacy.get_multi_inactive(db, skip=skip, limit=limit)

    return pharmacies


@router.post("/", response_model=schemas.Pharmacy)
def create_pharmacy(
    *,
    db: Session = Depends(deps.get_db),
    pharmacy_in: schemas.PharmacyCreate,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Create new pharmacy with owner.
    """
    if current_user.is_owner and current_user.pharmacy_id is None:
        pharmacy = crud.pharmacy.create(db=db, obj_in=pharmacy_in)
        pharmacy.users.append(crud.user.get(db, current_user.id))
        db.commit()
    elif current_user.pharmacy_id is not None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="User has already a pharmacy",
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User is not owner",
        )
    return pharmacy


@router.put("/", response_model=schemas.Pharmacy)
def update_pharmacy(
    *,
    db: Session = Depends(deps.get_db),
    pharmacy_in: schemas.PharmacyUpdate,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Update an pharmacy.
    """
    if not current_user.is_owner:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions")
        
    if current_user.pharmacy_id is None:
        raise HTTPException(status_code=422, detail="User has no linked pharmacy")

    pharmacy = crud.pharmacy.get(db=db, id=current_user.pharmacy_id) 
        
    pharmacy = crud.pharmacy.update(db=db, db_obj=pharmacy, obj_in=pharmacy_in)
    return pharmacy


@router.get("/me", response_model=schemas.Pharmacy)
def read_pharmacy_me(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Get pharmacy of the current_user.
    """
    pharmacy = current_user.pharmacy
    if not pharmacy:
        raise HTTPException(status_code=404, detail="User has no pharmacy")
    return pharmacy


@router.get("/owner", response_model=schemas.User)
def read_pharmacy_owner(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Get owner of the current_user's pharmacy [only available for the owner of the pharmacy].
    """
    pharmacy = crud.user.get(db=db, id=current_user.id).pharmacy
    if not pharmacy:
        raise HTTPException(status_code=404, detail="User has no pharmacy")
    if not current_user.is_owner:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
            )
    
    return pharmacy.get_owner()


@router.get("/employees", response_model=List[schemas.User])
def read_pharmacy_employees(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Get employees of the current_user's pharmacy.
    """
    pharmacy = crud.user.get(db=db, id=current_user.id).pharmacy
    if not pharmacy:
        raise HTTPException(status_code=404, detail="User has no pharmacy")
    return pharmacy.get_employees().all()


@router.get("/customers", response_model=List[schemas.User])
def read_pharmacy_customers(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Get customers of the current_user's pharmacy.
    """
    pharmacy = crud.user.get(db=db, id=current_user.id).pharmacy
    if not pharmacy:
        raise HTTPException(status_code=404, detail="User has no pharmacy")
    if not current_user.is_owner or not current_user.is_employee :
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
            )

    return pharmacy.get_customers().all()


@router.post("/selection", response_model=schemas.Pharmacy)    
def select_pharmacy_customer(
    pharmacy_id: UUID4,
    current_user: models.User = Depends(deps.get_current_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Select a pharmacy as a customer
    """
    if not current_user.is_customer:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User has to be a customer to select a pharmacy"
            )
    pharmacy = crud.pharmacy.get(db=db, id=pharmacy_id)
    if pharmacy is None:
        raise HTTPException(status_code=404, detail="No such pharmacy")
    crud.user.select_pharmacy(db=db, db_user=current_user, db_pharmacy=pharmacy)
    return pharmacy

