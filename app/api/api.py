from app.api import atlas

from fastapi import APIRouter

router = APIRouter()

router.include_router(atlas.router, prefix="/atlas", tags=["Atlas"])