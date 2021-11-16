from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile, Body
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
    filter: str = ""
) -> Any:
    """
    Retrieve active pharmacies.
    """
    pharmacies = crud.pharmacy.get_multi_active(
        db, skip=skip, limit=limit, filter=filter)
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
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User has no pharmacy")
    return pharmacy


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
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User has no pharmacy")
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
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User has no pharmacy"
        )
    if not current_user.is_owner or not current_user.is_employee:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )

    return pharmacy.get_customers().all()


@router.post("/selection", response_model=schemas.Pharmacy)
def select_pharmacy_customer(
    pharmacy_id: UUID4 = Body(..., embed=True),
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
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No such pharmacy")
    crud.user.select_pharmacy(db=db, db_user=current_user, db_pharmacy=pharmacy)
    return pharmacy


@router.post("/selection/image")
def define_selection_image(
    image: UploadFile = File(...),
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """Upload an image to use as the selection image for the current_user's pharmacy"""
    if not (current_user.is_admin or current_user.is_owner):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Current user has not enough priviledges"
        )
    if not current_user.pharmacy_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User has no linked pharmacy"
        )
    return {'success': True, 'msg': 'The image was uploaded succefully', 'image': 'https://img.bfmtv.com/c/630/420/871/7b9f41477da5f240b24bd67216dd7.jpg'}


@router.post("/presentation/image")
def define_presentation_image(
    image: UploadFile = File(...),
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """Upload an image to use on the presentation page for the current_user's pharmacy"""
    if not (current_user.is_admin or current_user.is_owner):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Current user has not enough priviledges"
        )
    if not current_user.pharmacy_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User has no linked pharmacy"
        )
    return {'success': True, 'msg': 'The image was uploaded succefully', 'image': 'https://img.bfmtv.com/c/630/420/871/7b9f41477da5f240b24bd67216dd7.jpg'}
