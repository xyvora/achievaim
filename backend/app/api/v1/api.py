from app.api.v1.routes import goal, health, user
from app.utils import APIRouter

api_router = APIRouter()
api_router.include_router(goal.router)
api_router.include_router(health.router)
api_router.include_router(user.router)
