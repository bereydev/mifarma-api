from fastapi import APIRouter

from app.api.api_v1.endpoints import drugs, login, owner, pharmacies, users, utils, products, shop, settings

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(drugs.router, prefix="/drugs", tags=["drugs"])
api_router.include_router(products.router, prefix="/products", tags=["products"])
api_router.include_router(pharmacies.router, prefix="/pharmacies", tags=["pharmacies"])
api_router.include_router(shop.router, prefix="/shop", tags=["shop"])
api_router.include_router(settings.router, prefix="/settings", tags=["settings"])
api_router.include_router(owner.router, prefix="/owner", tags=["owner"])
