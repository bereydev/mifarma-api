from app.models.role import RoleName
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile
from pydantic.types import UUID4
from sqlalchemy.orm import Session
from app.models import Role

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Product])
def read_products(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Retrieve products of a user's pharmacy
    """
    products = crud.product.get_multi_by_pharmacy(
        db=db, pharmacy_id=current_user.pharmacy_id, skip=skip, limit=limit
    )
    return products


@router.post("/", response_model=schemas.Product)
def create_product(
    *,
    db: Session = Depends(deps.get_db),
    product_in: schemas.ProductCreate,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Create new product in the catalog.
    """
    if not current_user.is_owner:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Don't have enough permission to add product to the catalog",
        )
    if current_user.pharmacy_id is not None:
        product = crud.product.create_with_pharmacy(
            db=db, obj_in=product_in, pharmacy_id=current_user.pharmacy_id)
    else:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Current user has no attributed pharmacy",
        )
    return product


@router.put("/{id}", response_model=schemas.Product)
def update_product(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID4,
    product_in: schemas.ProductUpdate,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Update an product.
    """
    product = crud.product.get(db=db, id=id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Product not found")
    if not current_user.is_owner:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    product = crud.product.update(db=db, db_obj=product, obj_in=product_in)
    return product


@router.get("/{id}", response_model=schemas.Product)
def read_product(
    *,
    db: Session = Depends(deps.get_db),
    id: UUID4,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Get product by ID.
    """
    product = crud.product.get(db=db, id=id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Product not found")
    if not current_user.is_admin and (product.owner_id != current_user.id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    return product


@router.delete("/{id}", response_model=schemas.Product)
def delete_product(
    *,
    id: UUID4,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Delete an product.
    """
    product = crud.product.get(db=db, id=id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Product not found")
    if not crud.user.is_admin(current_user) and (product.owner_id != current_user.id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    product = crud.product.remove(db=db, id=id)
    return product


@router.get("/ean/{ean_code}", response_model=schemas.Product)
def get_by_ean(
    ean_code: str,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Retrieve a product by its ean
    """
    product = crud.product.get_by_ean(db, ean_code)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The requested ean does not match any product in the catalog"
        )
    return product


@router.post("/image")
async def upload_product_image(
    product_id: UUID4,
    upload_image: UploadFile = File(...),
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """Upload an image for the current_user's pharmacy"""
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

    # Check the mime type
    if not upload_image.content_type in ["image/jpeg", "image/png"]:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="File type is not PNG or JPEG"
        )

    product = crud.product.get(db, product_id)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No product is linked to the provided id"
        )

    image = crud.image.create(db=db,
                              obj_in=schemas.ImageCreate(
                                  product_id=product.id,
                                   name=f'product_{product.ean_code}_image'),
                              upload_image=upload_image,
                              old_image=product.image
                              )

    return {'success': True, 'msg': 'The image was uploaded succefully', 'image': image.filename}
