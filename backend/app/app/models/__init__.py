from app.models import pharmacy
from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401
    
from .user import User
from .drug import Drug
from .product import Product
from .pharmacy import Pharmacy
from .role  import Role