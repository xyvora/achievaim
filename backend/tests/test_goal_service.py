import pytest
from bson import ObjectId

from app.exceptions import DuplicateGoalError, UserNotFoundError
from app.models.user import Goal, GoalCreate
from app.services.goal_service import (
    create_goal,
    delete_goal_by_id,
    delete_goal_by_name,
    get_goal_by_id,
    get_goal_by_name,
    update_goal,
)


async def test_delete_goal_by_id_user_not_found():
    with pytest.raises(UserNotFoundError):
        await delete_goal_by_id(ObjectId(), "some id")


async def test_delete_goal_by_name_user_not_found():
    with pytest.raises(UserNotFoundError):
        await delete_goal_by_name(ObjectId(), "some goal")


async def test_create_goal_user_not_found():
    with pytest.raises(UserNotFoundError):
        await create_goal(ObjectId(), GoalCreate(id="some id", goal="some goal"))


async def test_get_goal_by_id_user_not_found():
    with pytest.raises(UserNotFoundError):
        await get_goal_by_id(ObjectId(), "some id")


async def test_get_goal_by_name_user_not_found():
    with pytest.raises(UserNotFoundError):
        await get_goal_by_name(ObjectId(), "some name")


async def test_update_goal_user_not_found():
    with pytest.raises(UserNotFoundError):
        await update_goal(ObjectId(), Goal(id="someid", goal="some goal"))


async def test_update_goal_duplicate_goal(user_with_goals):
    with pytest.raises(DuplicateGoalError):
        await update_goal(
            user_with_goals.id,
            Goal(id=user_with_goals.goals[0].id, goal=user_with_goals.goals[1].goal),
        )
