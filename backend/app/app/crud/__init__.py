from .crud_user import user
from .crud_drug import drug
from .crud_pharmacy import pharmacy
from .crud_product import product
from .crud_stock_item import stock_item
from .crud_order import order

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models import Item
# from app.schemas import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
