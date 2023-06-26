from app.api.v1.routes import health
from app.utils import APIRouter

api_router = APIRouter()
api_router.include_router(health.router)
