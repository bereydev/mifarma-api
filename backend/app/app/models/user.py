from typing import List, TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, Date, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy import true

from app.db.base_class import Base
from .role import Permission
import uuid
from .order import Order, OrderStatus
from sqlalchemy.ext.hybrid import hybrid_property

if TYPE_CHECKING:
    from .order import Order
    from .image import Image


class Gender():
    male = 0
    female = 1
    non_binary = 2
    not_specified = 3


class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    public_id = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    role_id = Column(UUID(as_uuid=True), ForeignKey('roles.id'))
    phone = Column(String)
    gender = Column(Integer, default=Gender.not_specified, nullable=False)
    pregnant = Column(Boolean())
    birthdate = Column(Date)
    # Weight in kg
    weight = Column(Integer)
    # Height in mm
    height = Column(Integer)
    # List of Allergies with the following format "{<name of the allergie>:<true or false>,...}"
    allergies = Column(MutableDict.as_mutable(JSON), default={}, nullable=False)
    smoker = Column(Boolean())
    addict = Column(Boolean())
    alcoholic = Column(Boolean())
    hashed_password = Column(String, nullable=False)
    address = Column(String)
    postcode = Column(String)
    city = Column(String)
    country = Column(String)
    # List of current use of drugs and prescriptions of the following format "{'prescriptions':[<names>,...]}"
    prescriptions = Column(MutableDict.as_mutable(JSON), default={
                           'prescriptions': []}, nullable=False)
    # List of previous diseases with the following format "{<name of the diseases>:<true or false>,...}"
    previous_diseases = Column(MutableDict.as_mutable(JSON), default={}, nullable=False)
    # None if the user is not Owner, has to be checked manualy by a MiFarmacia staff before activating the account
    pharmacist_number = Column(String)
    pharmacy_id = Column(UUID(as_uuid=True), ForeignKey('pharmacies.id'))
    orders = relationship('Order', backref='user', lazy='dynamic')
    # Account validation elements
    # Adress mail confirmed
    confirmed = Column(Boolean(), default=False, nullable=False)
    # Owner account validated by a staff (with ID image and pharmacist_number verification)
    verified = Column(Boolean(), default=True, nullable=False)
    # Owner account and physical address validated by letter with a 15 days valid token
    activated = Column(Boolean(), default=True, nullable=False)
    refused = Column(Boolean(), default=False, nullable=False)
    # Activation token sent over letter hashed with the user credentials and a expiration time
    hashed_activation_token = Column(String)
    image = relationship('Image', backref='user', uselist=False)

    @hybrid_property
    def image_filename(self):
        return self.image.filename

    def can(self, perm):
        return self.role is not None and self.role.has_permission(perm)

    @hybrid_property
    def is_owner(self):
        return self.can(Permission.OWN)

    @hybrid_property
    def is_admin(self):
        return self.can(Permission.ADMIN)

    @hybrid_property
    def is_customer(self):
        return self.can(Permission.BUY)

    @hybrid_property
    def is_employee(self):
        return self.can(Permission.SELL)

    def get_cart(self) -> List[Order]:
        return self.orders.filter(Order.status == OrderStatus.in_cart).all()

    @hybrid_property
    def voucher(self) -> float:
        # return self.orders.filter(Order.count_for_voucher == true()).sum(Order.count_for_voucher)
        return sum(order.product.price
                   for order
                   in self.orders.filter(Order.count_for_voucher == true())
                   ) * self.pharmacy.percentage_for_voucher / 100
