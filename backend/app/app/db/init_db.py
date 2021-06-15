from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.config import settings
# from app.db import base  # noqa: F401
from app.db.session import engine
from app.models.role import Permission, RoleName, Role

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def insert_roles(db: Session):
    roles = {
        RoleName.CUSTOMER: [Permission.BUY],
        RoleName.EMPLOYEE: [Permission.SELL],
        RoleName.OWNER: [Permission.SELL, Permission.OWN],
        RoleName.ADMIN: [Permission.BUY, Permission.SELL, Permission.OWN, Permission.ADMIN]
    }
    for r in roles:
        role = db.query(Role).filter_by(name=r).first()
        if role is None:
            role = Role(name=r)
        role.reset_permission()
        for perm in roles[r]:
            role.add_permission(perm)
        db.add(role)
    db.commit()


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the two next lines

    # base.Base.metadata.drop_all(bind=engine)
    # base.Base.metadata.create_all(bind=engine)

    pass
    # insert_roles(db)
    # user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    # if not user:
    #     user_in = schemas.UserCreate(
    #         email=settings.FIRST_SUPERUSER,
    #         password=settings.FIRST_SUPERUSER_PASSWORD,
    #         first_name='Jonathan',
    #         last_name='Bereyziat'
    #     )
    #     user = crud.user.create_with_role(db, obj_in=user_in, role=RoleName.ADMIN)  # noqa: F841

