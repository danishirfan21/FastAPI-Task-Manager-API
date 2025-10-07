

from fastapi import APIRouter
from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.tasks import router as tasks_router

api_router = APIRouter()
api_router.include_router(auth_router)
api_router.include_router(tasks_router)
