from fastapi import APIRouter

from .user import router as user_router
from .product import router as products_router

router = APIRouter(prefix="/v1")
router.include_router(user_router)
router.include_router(products_router)
