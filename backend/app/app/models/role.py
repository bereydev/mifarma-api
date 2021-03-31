from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401

class Permission:
    # Usual user of the app
    BUY = 1
    # Selling drugs and handle the orders
    SELL = 2
    # Manage the pharmacy informations
    OWN = 4
    # Moderator
    ADMIN = 8


class RoleName:
    CUSTOMER = 'Customer'
    EMPLOYEE = 'Employee'
    OWNER = 'Owner'
    ADMIN = 'Administrator'

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    permissions = Column(Integer, default=0)
    users = relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return f'<Role {self.name} level of permissions {self.permissions}>'

    def add_permission(self, perm):
        if not self.has_permission(perm):
            self.permissions += perm

    def remove_permission(self, perm):
        if self.has_permission(perm):
            self.permissions -= perm

    def reset_permission(self):
        self.permissions = 0

    def has_permission(self, perm):
        return self.permissions & perm == perm

    @classmethod
    def get_role_id(cls, role_name: RoleName) -> int:
        return cls.query.filter(cls.name == role_name).first().id

    # @staticmethod
    # def insert_roles():
    #     roles = {
    #         RoleName.CUSTOMER: [Permission.BUY],
    #         RoleName.EMPLOYEE: [Permission.SELL],
    #         RoleName.OWNER: [Permission.SELL, Permission.OWN],
    #         RoleName.ADMIN: [Permission.ADMIN]
    #     }
    #     for r in roles:
    #         role = Role.query.filter_by(name=r).first()
    #         if role is None:
    #             role = Role(name=r)
    #         role.reset_permission()
    #         for perm in roles[r]:
    #             role.add_permission(perm)
    #         session.add(role)
    #     session.commit()