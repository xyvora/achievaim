from copy import deepcopy
from uuid import uuid4

import pytest


@pytest.mark.usefixtures("user_no_goals")
async def test_create_goal_no_goals(test_client, user_data, user_token_headers):
    goal_data = deepcopy(user_data["goals"][0])
    response = await test_client.post("goal/", headers=user_token_headers, json=goal_data)
    response_json = response.json()

    assert len(response_json) == 1
    assert "id" in response_json[0]

    got = response_json[0]
    got.pop("id")
    got["goal_date"] = got["goal_date"].split(".", maxsplit=1)[0]
    user_data["goals"][0].pop("id")
    for goal in user_data["goals"]:
        if goal.get("goal_date"):
            goal["goal_date"] = goal["goal_date"].split(".", maxsplit=1)[0]

    assert sorted(got.items()) == sorted(user_data["goals"][0].items())


@pytest.mark.usefixtures("user_with_goals")
async def test_create_goal_with_goals(test_client, user_data, user_token_headers):
    goal_data = deepcopy(user_data["goals"][0])
    goal_data["goal"] = str(uuid4())
    response = await test_client.post("goal/", headers=user_token_headers, json=goal_data)

    got = []
    for goal in response.json():
        if goal["goal_date"]:
            goal["goal_date"] = goal["goal_date"].split(".", maxsplit=1)[0]
        goal.pop("id")
        got.append(goal)

    expected = []
    for goal in user_data["goals"]:
        goal.pop("id")
        if goal.get("goal_date"):
            goal["goal_date"] = goal["goal_date"].split(".", maxsplit=1)[0]
        else:
            goal["goal_date"] = None
        expected.append(goal)

    goal_data.pop("id")
    goal_data["goal_date"] = goal_data["goal_date"].split(".", maxsplit=1)[0]
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
    assert f"No goal with the id {goal_id} found" == response.json()["detail"]


async def test_delete_goal_by_name(test_client, user_with_goals, user_token_headers):
    response = await test_client.delete(
        f"goal/goal-name/{user_with_goals.goals[0].goal}", headers=user_token_headers
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
    assert f"No goal with the name {goal_name} found" == response.json()["detail"]


async def test_get_all_goals(test_client, user_with_goals, user_token_headers):
    response = await test_client.get("goal", headers=user_token_headers)
    assert response.json()[0]["goal"] == user_with_goals.goals[0].goal


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
    assert response.json()["goal"] == user_with_goals.goals[0].goal


async def test_get_goal_by_name(test_client, user_with_goals, user_token_headers):
    response = await test_client.get(
        f"goal/goal-name/{user_with_goals.goals[0].goal}", headers=user_token_headers
    )
    assert response.json()["goal"] == user_with_goals.goals[0].goal


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
    goal_data["goal"] = "Test"
    response = await test_client.put("goal/", json=goal_data, headers=user_token_headers)
    goals = [x["goal"] for x in response.json()]
    assert "Test" in goals


async def test_update_goal_user_not_authenticated(test_client, user_data):
    goal_data = deepcopy(user_data["goals"][0])
    response = await test_client.put("goal/", json=goal_data)
    assert response.status_code == 401


@pytest.mark.usefixtures("user_no_goals")
async def test_update_goal_no_goals(test_client, user_data, user_token_headers):
    goal_data = deepcopy(user_data["goals"][0])
    response = await test_client.put("goal/", headers=user_token_headers, json=goal_data)
    assert response.status_code == 404
    assert "No goals found for user" == response.json()["detail"]


@pytest.mark.usefixtures("user_with_goals")
async def test_update_goal_goal_not_found(test_client, user_data, user_token_headers):
    goal_data = deepcopy(user_data["goals"][0])
    goal_data["id"] = str(uuid4())
    goal_data["goal"] = str(uuid4())
    response = await test_client.put("goal/", headers=user_token_headers, json=goal_data)
    assert response.status_code == 404
    assert "No goals found for user" == response.json()["detail"]


@pytest.mark.usefixtures("user_with_goals")
async def test_update_goal_duplicate_goal(test_client, user_data, user_token_headers):
    goal_data = deepcopy(user_data["goals"][0])
    goal_data["goal"] = user_data["goals"][1]
    response = await test_client.put("goal/", json=goal_data, headers=user_token_headers)
    assert response.status_code == 422
