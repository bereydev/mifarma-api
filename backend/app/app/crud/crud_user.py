from app.models.role import Role, RoleName
from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models import User, Role
from app.schemas.user import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def create_with_role(self, db: Session, obj_in: UserCreate, role: RoleName) -> User:
        user_in_data = jsonable_encoder(obj_in)
        user_in_data['hashed_password'] = get_password_hash(user_in_data.pop('password'))
        user_in_data['role_id'] = db.query(Role).filter(Role.name == role).first().id

        db_obj = User(**user_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def create_customer(self, db: Session, user_in: UserCreate) -> User:
        user = self.create_with_role(db, user_in, RoleName.CUSTOMER)
        user.confirmed = False
        user.verified = True
        user.activated = True
        db.commit()
        return user
    
    def create_owner(self, db: Session, user_in: User) -> User:
        user = self.create_with_role(db, user_in, RoleName.OWNER)
        user.confirmed = False
        user.verified = False
        user.activated = False
        db.commit()
        return user
    
    def create_employee(self, db: Session, *, user_in: User) -> User:
        user = self.create_with_role(db, user_in, RoleName.EMPLOYEE)
        user.confirmed = False
        user.verified = False
        user.activated = False
        db.commit()
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
    
    def confirm(self, db: Session, user: User) -> User:
        user.confirmed = True
        db.commit()
        return user
    
    def validate(self, db: Session, user: User) -> User:
        user.verified = True
        db.commit()
        return user
    
    def activate(self, db: Session, user: User) -> User:
        user.activated = True
        db.commit()
        return user

    def is_admin(self, user: User) -> bool:
        return user.role.name == RoleName.ADMIN


user = CRUDUser(User)
