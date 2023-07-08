from copy import deepcopy
from uuid import uuid4

import pytest
from bson import ObjectId
from fastapi import HTTPException

from app.api.v1.routes.goal import _validate_unique_goal


@pytest.mark.usefixtures("user_no_goals")
async def test_create_goal_no_goals(test_client, user_data):
    goal_data = deepcopy(user_data["goals"][0])
    goal_data["user_id"] = user_data["_id"]
    response = await test_client.post("goal/", json=goal_data)
    response_json = response.json()

    assert len(response_json) == 1
    assert "id" in response_json[0]

    got = response_json[0]
    got.pop("id")
    user_data["goals"][0].pop("id")
    assert sorted(got.items()) == sorted(user_data["goals"][0].items())


@pytest.mark.usefixtures("user_with_goals")
async def test_create_goal_with_goals(test_client, user_data):
    goal_data = deepcopy(user_data["goals"][0])
    goal_data["name"] = str(uuid4())
    goal_data["user_id"] = user_data["_id"]
    response = await test_client.post("goal/", json=goal_data)

    got = []
    for goal in response.json():
        goal.pop("id")
        got.append(goal)

    expected = []
    for goal in user_data["goals"]:
        goal.pop("id")
        expected.append(goal)

    goal_data.pop("user_id")
    goal_data.pop("id")
    expected.append(goal_data)

    assert [sorted(x.items()) for x in got] == [sorted(x.items()) for x in expected]


@pytest.mark.usefixtures("user_with_goals")
async def test_create_goal_duplicate(test_client, user_data):
    goal_data = deepcopy(user_data["goals"][0])
    goal_data["user_id"] = user_data["_id"]
    response = await test_client.post("goal/", json=goal_data)
    assert response.status_code == 400


async def test_create_goal_user_not_found(test_client, user_data):
    goal_data = deepcopy(user_data["goals"][0])
    goal_data["user_id"] = user_data["_id"]
    response = await test_client.post("goal/", json=goal_data)
    assert response.status_code == 404
    assert "User with ID" in response.json()["detail"]


async def test_delete_goal_by_id(test_client, user_with_goals):
    response = await test_client.delete(f"goal/{user_with_goals.id}/{user_with_goals.goals[0].id}")
    assert response.status_code == 204


async def test_delete_goal_by_id_user_not_found(test_client):
    response = await test_client.delete(f"goal/{ObjectId()}/some_goal")
    assert response.status_code == 404
    assert "User not found" == response.json()["detail"]


async def test_delete_goal_by_id_no_goals(test_client, user_no_goals):
    response = await test_client.delete(f"goal/{user_no_goals.id}/some_goal")
    assert response.status_code == 404
    assert "No goals found for user" == response.json()["detail"]


async def test_delete_goal_by_id_not_found(test_client, user_with_goals):
    goal_id = str(uuid4())
    response = await test_client.delete(f"goal/{user_with_goals.id}/{goal_id}")
    assert response.status_code == 404
    assert f"Goal {goal_id} not found" == response.json()["detail"]


async def test_delete_goal_by_id_invalid_oid(test_client):
    response = await test_client.delete("goal/bad/bad")
    assert response.status_code == 400


async def test_delete_goal_by_name(test_client, user_with_goals):
    response = await test_client.delete(
        f"goal/{user_with_goals.id}/goal-name/{user_with_goals.goals[0].name}"
    )
    assert response.status_code == 204


async def test_delete_goal_by_name_user_not_found(test_client):
    response = await test_client.delete(f"goal/{ObjectId()}/goal-name/some_goal")
    assert response.status_code == 404
    assert "User not found" == response.json()["detail"]


async def test_delete_goal_by_name_no_goals(test_client, user_no_goals):
    response = await test_client.delete(f"goal/{user_no_goals.id}/goal-name/some_goal")
    assert response.status_code == 404
    assert "No goals found for user" == response.json()["detail"]


async def test_delete_goal_by_name_not_found(test_client, user_with_goals):
    goal_name = str(uuid4())
    response = await test_client.delete(f"goal/{user_with_goals.id}/goal-name/{goal_name}")
    assert response.status_code == 404
    assert f"Goal {goal_name} not found" == response.json()["detail"]


async def test_delete_goal_by_name_invalid_oid(test_client):
    response = await test_client.delete("goal/bad/goal-name/some_goal")
    assert response.status_code == 400


async def test_get_all_goals(test_client, user_with_goals):
    response = await test_client.get(f"goal/{user_with_goals.id}")
    assert response.json()[0]["name"] == user_with_goals.goals[0].name


async def test_get_all_goals_no_goals(test_client, user_no_goals):
    response = await test_client.get(f"goal/{user_no_goals.id}")
    assert response.status_code == 404


async def test_get_all_goals_user_not_found(test_client):
    response = await test_client.get(f"goal/{ObjectId()}")
    assert response.status_code == 404


async def test_get_all_goals_bad_oid(test_client):
    response = await test_client.get("goal/bad")
    assert response.status_code == 400


async def test_get_by_id_user_not_found(test_client):
    response = await test_client.get(f"goal/{ObjectId()}/someid")
    assert response.status_code == 404
    assert "User not found" == response.json()["detail"]


async def test_get_goal_by_id_not_found(test_client, user_with_goals):
    response = await test_client.get(f"goal/{user_with_goals.id}/some_id")
    assert response.status_code == 404
    assert "No goal ID" in response.json()["detail"]


async def test_get_goal_by_id_no_goals(test_client, user_no_goals):
    response = await test_client.get(f"goal/{user_no_goals.id}/some_id")
    assert response.status_code == 404
    assert "No goals found for user" == response.json()["detail"]


async def test_get_goal_by_id_bad_oid(test_client):
    response = await test_client.get("goal/bad/bad")
    assert response.status_code == 400


async def test_get_goal_by_id(test_client, user_with_goals):
    response = await test_client.get(f"goal/{user_with_goals.id}/{user_with_goals.goals[0].id}")
    assert response.json()["name"] == user_with_goals.goals[0].name


async def test_get_goal_by_name(test_client, user_with_goals):
    response = await test_client.get(
        f"goal/{user_with_goals.id}/goal-name/{user_with_goals.goals[0].name}"
    )
    assert response.json()["name"] == user_with_goals.goals[0].name


async def test_get_goal_by_name_not_found(test_client, user_with_goals):
    response = await test_client.get(f"goal/{user_with_goals.id}/goal-name/bad")
    assert response.status_code == 404
    assert "No goal named" in response.json()["detail"]


async def test_get_goal_by_name_no_goals(test_client, user_no_goals):
    response = await test_client.get(f"goal/{user_no_goals.id}/goal-name/bad")
    assert response.status_code == 404
    assert "No goals found for user" == response.json()["detail"]


async def test_get_goal_by_name_user_not_found(test_client):
    response = await test_client.get(f"goal/{ObjectId()}/goal-name/bad")
    assert response.status_code == 404
    assert "User not found" == response.json()["detail"]


async def test_get_goal_by_name_bad_oid(test_client):
    response = await test_client.get("goal/bad/goal-name/some_goal")
    assert response.status_code == 400


async def test_update_goal(test_client, user_with_goals, user_data):
    goal_data = deepcopy(user_data["goals"][0])
    goal_data["user_id"] = str(user_with_goals.id)
    goal_data["name"] = "Test"
    response = await test_client.put("goal/", json=goal_data)
    assert response.json()["name"] == "Test"


async def test_update_goal_user_not_found(test_client, user_data):
    goal_data = deepcopy(user_data["goals"][0])
    goal_data["user_id"] = str(ObjectId())
    response = await test_client.put("goal/", json=goal_data)
    assert response.status_code == 404
    assert "User with ID" in response.json()["detail"]


async def test_update_goal_no_goals(test_client, user_no_goals, user_data):
    goal_data = deepcopy(user_data["goals"][0])
    goal_data["user_id"] = str(user_no_goals.id)
    response = await test_client.put("goal/", json=goal_data)
    assert response.status_code == 404
    assert "No goals found for user" in response.json()["detail"]


async def test_update_goal_goal_not_found(test_client, user_with_goals, user_data):
    goal_data = deepcopy(user_data["goals"][0])
    goal_data["user_id"] = str(user_with_goals.id)
    goal_data["id"] = str(uuid4())
    goal_data["name"] = str(uuid4())
    response = await test_client.put("goal/", json=goal_data)
    assert response.status_code == 404
    assert "not found for user" in response.json()["detail"]


async def test_update_goal_bad_oid(test_client, user_data):
    goal_data = deepcopy(user_data["goals"][0])
    goal_data["user_id"] = "bad"
    response = await test_client.put("goal/", json=goal_data)
    assert response.status_code == 422


def test_validate_unique_goal_id(user_with_goals):
    with pytest.raises(HTTPException) as exc:
        _validate_unique_goal(user_with_goals, str(uuid4()), user_with_goals.goals[0].id)

    assert "Goal IDs must be unique" == exc.value.detail


def test_validate_unique_goal_name(user_with_goals):
    with pytest.raises(HTTPException) as exc:
        _validate_unique_goal(user_with_goals, user_with_goals.goals[0].name)

    assert "Goal names must be unique" == exc.value.detail
