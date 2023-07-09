from app.api.v1.routes import goal, health, login, user
from app.core.utils import APIRouter

api_router = APIRouter()
api_router.include_router(goal.router)
api_router.include_router(health.router)
api_router.include_router(login.router)
api_router.include_router(user.router)
