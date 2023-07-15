from beanie import PydanticObjectId
from bson import ObjectId

from app.models.user import Goal, User
from app.services.user_service import get_full_user


async def get_goal_by_id(user_id: ObjectId | PydanticObjectId, goal_id: str) -> Goal | None:
    user = await get_full_user(user_id)

    if not user:
        return None

    if not user.goals:
        return None

    for goal in user.goals:
        if goal.id == goal_id:
            return goal

    return None


async def get_goal_by_name(user_id: ObjectId | PydanticObjectId, goal_name: str) -> Goal | None:
    user = await get_full_user(user_id)

    if not user:
        return None

    if not user.goals:
        return None

    for goal in user.goals:
        if goal.name == goal_name:
            return goal

    return None


async def get_goals_by_user_id(user_id: ObjectId | PydanticObjectId) -> list[Goal] | None:
    user = await User.find_one(User.id == user_id)

    if not user or not user.goals:
        return None

    return user.goals
