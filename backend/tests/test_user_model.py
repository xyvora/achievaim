from copy import deepcopy
from uuid import uuid4

import pytest

from app.models.user import User


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
