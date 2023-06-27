import pytest
from bson import ObjectId


async def test_create_goal(test_client, goal_data):
    response = await test_client.post("goal/", json=goal_data)
    response_json = response.json()
    response_json.pop("_id")
    goal_data.pop("_id")

    assert response_json == goal_data


@pytest.mark.usefixtures("goal")
async def test_create_goal_duplicate(test_client, goal_data):
    response = await test_client.post("goal/", json=goal_data)
    assert response.status_code == 400


async def test_delete_goal_by_id(test_client, goal):
    response = await test_client.delete(f"goal/{goal.id}")
    assert response.status_code == 204


async def test_delete_goal_by_id_not_found(test_client):
    response = await test_client.delete(f"goal/{ObjectId()}")
    assert response.status_code == 404


async def test_delete_goal_by_id_invalid_oid(test_client):
    response = await test_client.delete("goal/bad")
    assert response.status_code == 400


async def test_delete_goal_by_name(test_client, goal):
    response = await test_client.delete(f"goal/name/{goal.name}")
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


async def test_update_goal(test_client, goal, goal_data):
    goal_data.pop("_id")
    goal_data["id"] = str(goal.id)
    goal_data["name"] = "Test"
    response = await test_client.put("goal/", json=goal_data)
    assert response.json()["name"] == goal_data["name"]


async def test_update_goal_not_found(test_client, goal_data):
    goal_data["id"] = goal_data.pop("_id")
    response = await test_client.put("goal/", json=goal_data)
    assert response.status_code == 404


async def test_update_goal_bad_oid(test_client, goal_data):
    goal_data.pop("_id")
    goal_data["id"] = "bad"
    goal_data["name"] = "Test"
    response = await test_client.put("goal/", json=goal_data)
    assert response.status_code == 400
