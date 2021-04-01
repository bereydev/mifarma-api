from .base import CRUDBase
from app.models import Product
from app.schemas import ProductCreate, ProductUpdate

product = CRUDBase[Product, ProductCreate, ProductUpdate](Product)