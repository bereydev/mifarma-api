from fastapi import UploadFile
from app.models.image import Image
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from .base import CRUDBase, CreateSchemaType, ModelType
from pydantic.types import UUID4
from app.models import Image
from app.schemas import ImageCreate, ImageUpdate
import PIL.Image as pilimg
from PIL import ExifTags
import os

IMAGE_MAX_SIZE = 500, 500
FILE_PATH = "/app/files/"


class CRUDImage(CRUDBase[Image, ImageCreate, ImageUpdate]):
    def create(self, db: Session, *, obj_in: CreateSchemaType, upload_image: UploadFile, old_image: Image) -> Image:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        image_path = FILE_PATH + db_obj.filename
        # Delete old image
        if old_image is not None:
            self.remove(db=db, id=old_image.id)
        process_image(image_path, upload_image)
        return db_obj

    def remove(self, db: Session, *, id: UUID4) -> ModelType:
        image = super().remove(db=db, id=id)
        try:
            os.remove(FILE_PATH + image.filename)
        except:
            pass
        return image


def process_image(image_path: str, upload_image: UploadFile):
    """Resize if necessary , compress and convert any image file into jpg, check also the 
    exif data to see if there is rotation modification to the image (smartphones and tablets issues)
    And save the processe file to the file system
    """
    # Open the file as an image to process it
    # with pilimg.open(image_path) as image:
    with pilimg.open(upload_image.file) as image:
        # Exif data check:
        try:
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation':
                    break

            exif = dict(image._getexif().items())

            if exif[orientation] == 3:
                image = image.rotate(180, expand=True)
            elif exif[orientation] == 6:
                image = image.rotate(270, expand=True)
            elif exif[orientation] == 8:
                image = image.rotate(90, expand=True)

        except (AttributeError, KeyError, IndexError):
            # cases: image don't have getexif
            pass
        image = image.convert('RGB')
        image = crop_max_square(image)
        image.thumbnail(IMAGE_MAX_SIZE, pilimg.ANTIALIAS)
        # Save the new image witht the same name
        image.save(image_path, 'JPEG', dpi=[300, 300], quality=80)
    
def crop_max_square(pil_img):
    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))

def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))


image = CRUDImage(Image)
