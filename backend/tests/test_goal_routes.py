from copy import deepcopy
from uuid import uuid4

import pytest
from fastapi import HTTPException

from app.api.v1.routes.goal import _validate_unique_goal


@pytest.mark.usefixtures("user_no_goals")
async def test_create_goal_no_goals(test_client, user_data, user_token_headers):
    goal_data = deepcopy(user_data["goals"][0])
    response = await test_client.post("goal/", headers=user_token_headers, json=goal_data)
    response_json = response.json()

    assert len(response_json) == 1
    assert "id" in response_json[0]

    got = response_json[0]
    got.pop("id")
    user_data["goals"][0].pop("id")
    assert sorted(got.items()) == sorted(user_data["goals"][0].items())


@pytest.mark.usefixtures("user_with_goals")
async def test_create_goal_with_goals(test_client, user_data, user_token_headers):
    goal_data = deepcopy(user_data["goals"][0])
    goal_data["name"] = str(uuid4())
    response = await test_client.post("goal/", headers=user_token_headers, json=goal_data)

    got = []
    for goal in response.json():
        goal.pop("id")
        got.append(goal)

    expected = []
    for goal in user_data["goals"]:
        goal.pop("id")
        expected.append(goal)

    goal_data.pop("id")
    expected.append(goal_data)

    assert [sorted(x.items()) for x in got] == [sorted(x.items()) for x in expected]


@pytest.mark.usefixtures("user_with_goals")
async def test_create_goal_duplicate(test_client, user_data, user_token_headers):
    goal_data = deepcopy(user_data["goals"][0])
    response = await test_client.post("goal/", headers=user_token_headers, json=goal_data)
    assert response.status_code == 400


async def tests_create_goal_not_authenticated(test_client, user_data):
    goal_data = deepcopy(user_data["goals"][0])
    response = await test_client.post("goal/", json=goal_data)
    assert response.status_code == 401


async def test_delete_goal_by_id(test_client, user_with_goals, user_token_headers):
    response = await test_client.delete(
        f"goal/{user_with_goals.goals[0].id}", headers=user_token_headers
    )
    assert response.status_code == 204


async def test_delete_goal_by_id_not_authenticated(test_client):
    response = await test_client.delete("goal/some_goal")
    assert response.status_code == 401


@pytest.mark.usefixtures("user_no_goals")
async def test_delete_goal_by_id_no_goals(test_client, user_token_headers):
    response = await test_client.delete("goal/some_goal", headers=user_token_headers)
    assert response.status_code == 404
    assert "No goals found for user" == response.json()["detail"]


@pytest.mark.usefixtures("user_with_goals")
async def test_delete_goal_by_id_not_found(test_client, user_token_headers):
    goal_id = str(uuid4())
    response = await test_client.delete(f"goal/{goal_id}", headers=user_token_headers)
    assert response.status_code == 404
    assert f"Goal {goal_id} not found" == response.json()["detail"]


async def test_delete_goal_by_name(test_client, user_with_goals, user_token_headers):
    response = await test_client.delete(
        f"goal/goal-name/{user_with_goals.goals[0].name}", headers=user_token_headers
    )
    assert response.status_code == 204


async def test_delete_goal_by_name_user_not_authenticated(test_client):
    response = await test_client.delete("goal/goal-name/some_goal")
    assert response.status_code == 401


@pytest.mark.usefixtures("user_no_goals")
async def test_delete_goal_by_name_no_goals(test_client, user_token_headers):
    response = await test_client.delete("goal/goal-name/some_goal", headers=user_token_headers)
    assert response.status_code == 404
    assert "No goals found for user" == response.json()["detail"]


@pytest.mark.usefixtures("user_with_goals")
async def test_delete_goal_by_name_not_found(test_client, user_token_headers):
    goal_name = str(uuid4())
    response = await test_client.delete(f"goal/goal-name/{goal_name}", headers=user_token_headers)
    assert response.status_code == 404
    assert f"Goal {goal_name} not found" == response.json()["detail"]


async def test_get_all_goals(test_client, user_with_goals, user_token_headers):
    response = await test_client.get("goal", headers=user_token_headers)
    assert response.json()[0]["name"] == user_with_goals.goals[0].name


@pytest.mark.usefixtures("user_no_goals")
async def test_get_all_goals_no_goals(test_client, user_token_headers):
    response = await test_client.get("goal/", headers=user_token_headers)
    assert response.status_code == 404


async def test_get_all_goals_user_not_authenticated(test_client):
    response = await test_client.get("goal/")
    assert response.status_code == 401


@pytest.mark.usefixtures("user_with_goals")
async def test_get_goal_by_id_not_found(test_client, user_token_headers):
    response = await test_client.get("goal/some_id", headers=user_token_headers)
    assert response.status_code == 404
    assert "No goal ID" in response.json()["detail"]


@pytest.mark.usefixtures("user_no_goals")
async def test_get_goal_by_id_no_goals(test_client, user_token_headers):
    response = await test_client.get("goal/some_id", headers=user_token_headers)
    assert response.status_code == 404
    assert "No goal ID" in response.json()["detail"]


async def test_get_goal_by_id(test_client, user_with_goals, user_token_headers):
    response = await test_client.get(
        f"goal/{user_with_goals.goals[0].id}", headers=user_token_headers
    )
    assert response.json()["name"] == user_with_goals.goals[0].name


async def test_get_goal_by_name(test_client, user_with_goals, user_token_headers):
    response = await test_client.get(
        f"goal/goal-name/{user_with_goals.goals[0].name}", headers=user_token_headers
    )
    assert response.json()["name"] == user_with_goals.goals[0].name


@pytest.mark.usefixtures("user_with_goals")
async def test_get_goal_by_name_not_found(test_client, user_token_headers):
    response = await test_client.get("goal/goal-name/bad", headers=user_token_headers)
    assert response.status_code == 404
    assert "No goal named" in response.json()["detail"]


@pytest.mark.usefixtures("user_no_goals")
async def test_get_goal_by_name_no_goals(test_client, user_token_headers):
    response = await test_client.get("goal/goal-name/bad", headers=user_token_headers)
    assert response.status_code == 404
    assert "No goal named" in response.json()["detail"]


async def test_get_goal_by_name_not_authenticated(test_client):
    response = await test_client.get("goal/goal-name/some_goal")
    assert response.status_code == 401


@pytest.mark.usefixtures("user_with_goals")
async def test_update_goal(test_client, user_data, user_token_headers):
    goal_data = deepcopy(user_data["goals"][0])
    goal_data["name"] = "Test"
    response = await test_client.put("goal/", json=goal_data, headers=user_token_headers)
    assert response.json()["name"] == "Test"


async def test_update_goal_user_not_authenticated(test_client, user_data):
    goal_data = deepcopy(user_data["goals"][0])
    response = await test_client.put("goal/", json=goal_data)
    assert response.status_code == 401


@pytest.mark.usefixtures("user_no_goals")
async def test_update_goal_no_goals(test_client, user_data, user_token_headers):
    goal_data = deepcopy(user_data["goals"][0])
    response = await test_client.put("goal/", headers=user_token_headers, json=goal_data)
    assert response.status_code == 404
    assert "No goals found for user" in response.json()["detail"]


@pytest.mark.usefixtures("user_with_goals")
async def test_update_goal_goal_not_found(test_client, user_data, user_token_headers):
    goal_data = deepcopy(user_data["goals"][0])
    goal_data["id"] = str(uuid4())
    goal_data["name"] = str(uuid4())
    response = await test_client.put("goal/", headers=user_token_headers, json=goal_data)
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]


def test_validate_unique_goal_id(user_with_goals):
    with pytest.raises(HTTPException) as exc:
        _validate_unique_goal(user_with_goals, str(uuid4()), user_with_goals.goals[0].id)

    assert "Goal IDs must be unique" == exc.value.detail


def test_validate_unique_goal_name(user_with_goals):
    with pytest.raises(HTTPException) as exc:
        _validate_unique_goal(user_with_goals, user_with_goals.goals[0].name)

    assert "Goal names must be unique" == exc.value.detail
