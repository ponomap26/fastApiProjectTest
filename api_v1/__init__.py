from fastapi import APIRouter
from .products.views import router as product_router
from .users.views import router as users_router
from .category.views import router as category_router

router = APIRouter()
router.include_router(router=category_router, prefix="/categorys")
router.include_router(router=users_router, prefix="/users")
router.include_router(router=product_router, prefix="/products")
