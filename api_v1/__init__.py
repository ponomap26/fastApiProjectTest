from fastapi import APIRouter

from core.models import User
from .auch.auch import auth_backend
from .auch.users.usermanager import get_user_manager
from .products.views import router as product_router
from api_v1.auch.users.views import router as users_router
from .category.views import router as category_router
from fastapi_users import fastapi_users

router = APIRouter()
router.include_router(router=category_router, prefix="/categorys")
router.include_router(router=users_router, prefix="/users")
router.include_router(router=product_router, prefix="/products")
# router.include_router(
#     fastapi_users.get_auth_router(
#         auth_backend, authenticator=auth_backend, get_user_manager=get_user_manager
#     ),
#     prefix="/auth",
#     tags=["auth"],
# )
