from fastapi import APIRouter

from backend.utils.config import settings
from .hiragana import router as hiragana_router

router = APIRouter(
    prefix=settings.api.prefix,
)

router.include_router(hiragana_router)
