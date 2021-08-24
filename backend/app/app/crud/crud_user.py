from app.schemas.customer import Customer
from pydantic.types import UUID4
from app.models.order import Order, OrderStatus
from app.schemas.pharmacy import Pharmacy
from app.models.role import Role, RoleName
from typing import Any, Dict, Optional, Union, List
import re

from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models import User, Role
from fastapi import HTTPException, status
from app.schemas import UserCreate, UserUpdate, OwnerUpdate, OwnerCreate, EmployeeCreate, CustomerCreate
import string
import random

def public_id_generator(size=6, chars=(string.ascii_uppercase + string.digits).replace('0','').replace('O','')):
    return ''.join(random.choice(chars) for _ in range(size))


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()
    
    def get_by_public_id(self, db: Session, *, public_id: str) -> Optional[User]:
        return db.query(User).filter(User.public_id == public_id).first()

    def create_with_role(self, db: Session, obj_in: UserCreate, role: RoleName) -> User:
        user_in_data = jsonable_encoder(obj_in)
        password_string = user_in_data.pop('password')
        # Check the passwork for 1 Majuscule 1 minuscule 8 char and 1 number
        if not re.match("^(?=.?[A-Z])(?=.?[a-z])(?=.*?[0-9]).{8,}$", password_string):
            raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Password does not match the required format"
            )
        user_in_data['hashed_password'] = get_password_hash(password_string)
        user_in_data['role_id'] = db.query(Role).filter(Role.name == role).first().id
        # Define a unique public id for the user
        public_id = public_id_generator()
        existing_user = self.get_by_public_id(db, public_id=public_id)
        while existing_user is not None:
            public_id = public_id_generator()
            existing_user = self.get_by_public_id(db, public_id=public_id)
        
        user_in_data['public_id'] = public_id

        db_obj = User(**user_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def create_customer(self, db: Session, user_in: CustomerCreate) -> User:
        user = self.create_with_role(db, user_in, RoleName.CUSTOMER)
        user.confirmed = False
        user.verified = True
        user.activated = True
        db.commit()
        db.refresh(user)
        return user
    
    def create_owner(self, db: Session, user_in: OwnerCreate) -> User:
        user = self.create_with_role(db, user_in, RoleName.OWNER)
        user.confirmed = False
        user.verified = False
        user.activated = False
        db.commit()
        db.refresh(user)
        return user
    
    def create_employee(self, db: Session, user_in: EmployeeCreate) -> User:
        user = self.create_with_role(db, user_in, RoleName.EMPLOYEE)
        user.confirmed = False
        user.verified = False
        user.activated = False
        db.commit()
        db.refresh(user)
        return user

    def create_admin(self, db: Session, user_in: EmployeeCreate) -> User:
        user = self.create_with_role(db, user_in, RoleName.ADMIN)
        user.confirmed = False
        user.verified = True
        user.activated = True
        db.commit()
        db.refresh(user)
        return user

    def update(
        self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data.get("password"):
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[User]:
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user
    
    def confirm(self, db: Session, db_user: User) -> User:
        db_user.confirmed = True
        db.commit()
        db.refresh(db_user)
        return db_user
    
    def verify(self, db: Session, db_user: User) -> User:
        db_user.verified = True
        db.commit()
        db.refresh(db_user)
        return db_user
    
    def activate(self, db: Session, db_user: User) -> User:
        db_user.activated = True
        db.commit()
        db.refresh(db_user)
        return db_user

    def select_pharmacy(self, db: Session, db_user: User, db_pharmacy: Pharmacy) -> Pharmacy:
        db_user.pharmacy_id = db_pharmacy.id
        db.commit()
        db.refresh(db_user)
        return db_user
    
    def get_customers_with_most_recent_placed_orders(self, db: Session, skip: int, limit: int, pharmacy_id: UUID4) -> List[User]:
        customers = db.query(User).join(Order).filter(Order.status == OrderStatus.placed).filter(User.pharmacy_id == pharmacy_id).order_by(Order.order_date.desc())
        return customers.offset(skip).limit(limit).all()
    
    def reset_voucher(self, db: Session, db_customer: Customer) -> Customer:
        for order in db_customer.orders:
            order.count_for_voucher = False
        db.commit()
        db.refresh(db_customer)
        return db_customer


user = CRUDUser(User)
