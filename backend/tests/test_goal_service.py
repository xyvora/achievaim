import pytest
from bson import ObjectId

from app.exceptions import UserNotFoundError
from app.models.user import GoalCreate
from app.services.goal_service import create_goal, get_goal_by_id, get_goal_by_name


async def test_create_goal_user_not_found():
    with pytest.raises(UserNotFoundError):
        await create_goal(ObjectId(), GoalCreate(id="some id", name="some goal"))


async def test_get_goal_by_id_user_not_found():
    with pytest.raises(UserNotFoundError):
        await get_goal_by_id(ObjectId(), "some id")


async def test_get_goal_by_name_user_not_found():
    with pytest.raises(UserNotFoundError):
        await get_goal_by_name(ObjectId(), "some name")
