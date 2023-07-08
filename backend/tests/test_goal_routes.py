from copy import deepcopy
from uuid import uuid4

import pytest
from bson import ObjectId


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


async def test_delete_goal_by_id(test_client, user):
    response = await test_client.delete(f"goal/{user.id}")
    assert response.status_code == 204


async def test_delete_goal_by_id_not_found(test_client):
    response = await test_client.delete(f"goal/{ObjectId()}")
    assert response.status_code == 404


async def test_delete_goal_by_id_invalid_oid(test_client):
    response = await test_client.delete("goal/bad")
    assert response.status_code == 400


async def test_delete_goal_by_name(test_client, user):
    response = await test_client.delete(f"goal/name/{user.goals[0].name}")
    assert response.status_code == 204


async def test_delete_goal_by_name_not_found(test_client):
    response = await test_client.delete("goal/name/bad")
    assert response.status_code == 404


async def test_get_all_goals(test_client, goal):
    response = await test_client.get("goal/")
    assert response.json()[0]["name"] == goal.name


async def test_get_goal_by_id(test_client, goal):
    response = await test_client.get(f"goal/{goal.id}")
    assert response.json()["name"] == goal.name


async def test_get_goal_by_id_not_found(test_client):
    response = await test_client.get(f"goal/{ObjectId()}")
    assert response.status_code == 404


async def test_get_goal_by_id_bad_oid(test_client):
    response = await test_client.get("goal/bad")
    assert response.status_code == 400


async def test_get_goal_by_name(test_client, goal):
    response = await test_client.get(f"goal/name/{goal.name}")
    assert response.json()["name"] == goal.name


async def test_get_goal_by_name_not_found(test_client):
    response = await test_client.get("goal/name/bad")
    assert response.status_code == 404


async def test_update_goal(test_client, goal, user_data):
    user_data.pop("_id")
    user_data["id"] = str(goal.id)
    user_data["name"] = "Test"
    response = await test_client.put("goal/", json=user_data)
    assert response.json()["name"] == user_data["name"]


async def test_update_goal_not_found(test_client, user_data):
    user_data["id"] = user_data.pop("_id")
    response = await test_client.put("goal/", json=user_data)
    assert response.status_code == 404


async def test_update_goal_bad_oid(test_client, user_data):
    user_data.pop("_id")
    user_data["id"] = "bad"
    user_data["name"] = "Test"
    response = await test_client.put("goal/", json=user_data)
    assert response.status_code == 400
