from copy import deepcopy
from uuid import uuid4

import pytest
from bson.errors import InvalidId

from app.models.user import GoalCreate, GoalWithUserId, User


def test_user_goal_duplicate_id_error(user_data):
    user_data["goals"].append(user_data["goals"][0])
    with pytest.raises(ValueError) as exc:
        User(**user_data)

    assert "Goal IDs must be unique" in str(exc.value)


def test_user_goal_duplicate_name_error(user_data):
    duplicate_goal = deepcopy(user_data["goals"])[0]
    duplicate_goal["id"] = str(uuid4())
    user_data["goals"].append(duplicate_goal)
    with pytest.raises(ValueError) as exc:
        User(**user_data)

    assert "Goal names must be unique" in str(exc.value)


@pytest.mark.parametrize("time", ["1212", "24:00", "-12:00", "12:60", "12:-01", "a:01", "01:a"])
def test_goal_invalid_time(time):
    with pytest.raises(ValueError):
        GoalCreate(goal="test", time_of_day=time)


def test_invalid_object_id():
    with pytest.raises(InvalidId):
        GoalWithUserId(user_id="bad", id="goal_id", goal="some goal")
