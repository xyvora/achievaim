from app.api.v1.routes import goal, health
from app.utils import APIRouter

api_router = APIRouter()
api_router.include_router(goal.router)
api_router.include_router(health.router)
