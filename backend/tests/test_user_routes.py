from uuid import uuid4

import pytest
from bson import ObjectId


@pytest.mark.parametrize("country", ["USA", None])
async def test_create_user(country, test_client):
    user_data = {
        "user_name": "arthurdent",
        "first_name": "Imma",
        "last_name": "User",
        "password": "immapassword",
        "security_question_answer": "my answer",
    }
    if country:
        user_data["country"] = country
    response = await test_client.post("user/", json=user_data)
    response_json = response.json()

    assert response_json["user_name"] == user_data["user_name"]


async def test_create_user_duplicate(user_with_goals, test_client):
    user_data = {
        "user_name": user_with_goals.user_name,
        "first_name": "Imma",
        "last_name": "User",
        "country": "USA",
        "password": "immapassword",
        "security_question_answer": "my answer",
    }
    response = await test_client.post("user/", json=user_data)

    assert response.status_code == 400


async def test_get_users(user_with_goals, test_client, superuser_token_headers):
    response = await test_client.get("user/", headers=superuser_token_headers)
    response_json = response.json()

    assert len(response_json) == 2
    assert response_json[0]["user_name"] == user_with_goals.user_name


@pytest.mark.usefixtures("user_with_goals")
async def test_get_users_not_admin(test_client, user_token_headers):
    response = await test_client.get("user/", headers=user_token_headers)

    assert response.status_code == 403
    assert "required permissions" in response.json()["detail"]


@pytest.mark.usefixtures("user_with_goals")
async def test_get_users_not_authenticated(test_client):
    response = await test_client.get("user/")

    assert response.status_code == 401


async def test_get_user_by_id(user_with_goals, test_client, superuser_token_headers):
    response = await test_client.get(f"user/{user_with_goals.id}", headers=superuser_token_headers)
    response_json = response.json()

    assert response_json["user_name"] == user_with_goals.user_name


async def test_get_user_by_id_bad_id(test_client, superuser_token_headers):
    response = await test_client.get("user/bad", headers=superuser_token_headers)

    assert response.status_code == 400
    assert "not a valid ID format" in response.json()["detail"]


async def test_get_user_by_id_not_admin(user_with_goals, test_client, user_token_headers):
    response = await test_client.get(f"user/{user_with_goals.id}", headers=user_token_headers)

    assert response.status_code == 403
    assert "required permissions" in response.json()["detail"]


async def test_get_user_by_id_not_authenticated(user_with_goals, test_client):
    response = await test_client.get(f"user/{user_with_goals.id}")

    assert response.status_code == 401


async def test_get_user_by_name(user_with_goals, test_client, superuser_token_headers):
    response = await test_client.get(
        f"user/user-name/{user_with_goals.user_name}", headers=superuser_token_headers
    )
    response_json = response.json()

    assert response_json["user_name"] == user_with_goals.user_name


async def test_get_user_by_name_not_found(test_client, superuser_token_headers):
    response = await test_client.get(f"user/user-name/{uuid4()}", headers=superuser_token_headers)

    assert response.status_code == 404


@pytest.mark.usefixtures("user_with_goals")
async def test_get_user_by_name_not_admin(test_client, user_token_headers):
    response = await test_client.get(f"user/user-name/{uuid4()}", headers=user_token_headers)

    assert response.status_code == 403
    assert "required permissions" in response.json()["detail"]


async def test_get_user_by_name_not_authenticated(test_client):
    response = await test_client.get(f"user/user-name/{uuid4()}")

    assert response.status_code == 401


async def test_get_me(test_client, user_with_goals, user_token_headers):
    response = await test_client.get("user/me", headers=user_token_headers)

    assert response.json()["id"] == str(user_with_goals.id)


async def test_get_me_not_authenticated(test_client):
    response = await test_client.get("user/me")

    assert response.status_code == 401


async def test_delete_user_by_id(user_with_goals, test_client, superuser_token_headers):
    response = await test_client.delete(
        f"user/{user_with_goals.id}", headers=superuser_token_headers
    )
    assert response.status_code == 204

    response = await test_client.get(f"user/{user_with_goals.id}", headers=superuser_token_headers)
    assert response.status_code == 404


async def test_delete_user_by_id_bad_id(test_client, superuser_token_headers):
    response = await test_client.delete("user/bad", headers=superuser_token_headers)
    assert response.status_code == 400
    assert "not a valid ID format" in response.json()["detail"]


async def test_delete_user_by_id_not_found(test_client, superuser_token_headers):
    response = await test_client.delete(f"user/{str(ObjectId())}", headers=superuser_token_headers)

    assert response.status_code == 404


async def test_delete_user_by_id_not_admin(test_client, user_with_goals, user_token_headers):
    response = await test_client.delete(f"user/{user_with_goals.id}", headers=user_token_headers)

    assert response.status_code == 403
    assert "required permissions" in response.json()["detail"]


async def test_delete_user_by_id_not_authenticated(test_client, user_with_goals):
    response = await test_client.delete(f"user/{user_with_goals.id}")

    assert response.status_code == 401


async def test_delete_user_by_user_name(user_with_goals, test_client, superuser_token_headers):
    response = await test_client.delete(
        f"user/user-name/{user_with_goals.user_name}", headers=superuser_token_headers
    )
    assert response.status_code == 204

    response = await test_client.get(f"user/{user_with_goals.id}", headers=superuser_token_headers)
    assert response.status_code == 404


async def test_delete_user_by_user_name_not_found(test_client, superuser_token_headers):
    response = await test_client.delete(
        f"user/user-name/{uuid4()}", headers=superuser_token_headers
    )

    assert response.status_code == 404


async def test_delete_user_by_user_name_not_admin(user_with_goals, test_client, user_token_headers):
    response = await test_client.delete(
        f"user/user-name/{user_with_goals.user_name}", headers=user_token_headers
    )
    assert response.status_code == 403
    assert "required permissions" in response.json()["detail"]


async def test_delete_user_by_user_name_not_authenticated(user_with_goals, test_client):
    response = await test_client.delete(f"user/user-name/{user_with_goals.user_name}")
    assert response.status_code == 401


async def test_delete_me(user_with_goals, test_client, user_token_headers, superuser_token_headers):
    response = await test_client.delete("user/me", headers=user_token_headers)
    assert response.status_code == 204

    response = await test_client.get(f"user/{user_with_goals.id}", headers=superuser_token_headers)
    assert response.status_code == 404


async def test_delete_me_not_authenticated(test_client):
    response = await test_client.delete("user/me")
    assert response.status_code == 401


async def test_update_me(user_with_goals, user_data, test_client, user_token_headers):
    user_data.pop("goals")
    user_data.pop("_id")
    user_data["password"] = "new_password"
    user_data["user_name"] = str(uuid4())
    user_data["id"] = str(user_with_goals.id)
    response = await test_client.put("user/me", headers=user_token_headers, json=user_data)

    assert response.json()["user_name"] == user_data["user_name"]


@pytest.mark.usefixtures("user_with_goals")
async def test_update_me_different_user(user_data, test_client, user_token_headers):
    response = await test_client.post(
        "user",
        json={
            "user_name": str(uuid4()),
            "first_name": "Imma",
            "last_name": "User",
            "country": "USA",
            "password": "abc",
            "security_question_answer": "my answer",
        },
    )
    assert response.status_code == 200
    user_data.pop("goals")
    user_data.pop("_id")
    user_data["password"] = "new_password"
    user_data["user_name"] = str(uuid4())
    user_data["id"] = response.json()["id"]
    response = await test_client.put("user/me", headers=user_token_headers, json=user_data)

    assert response.status_code == 400
    assert "Invalid user ID" == response.json()["detail"]


async def test_update_me_duplicate_user_name(test_client, user_with_goals, user_token_headers):
    user_data = {
        "user_name": str(uuid4()),
        "first_name": "Imma",
        "last_name": "User",
        "country": "USA",
        "password": "some_password",
        "security_question_answer": "my answer",
    }
    response = await test_client.post("user/", json=user_data)
    assert response.status_code == 200
    user_data["id"] = str(user_with_goals.id)
    response = await test_client.put("user/me", headers=user_token_headers, json=user_data)

    assert response.status_code == 400


async def test_update_me_not_authenticated(user_with_goals, user_data, test_client):
    user_data.pop("goals")
    user_data.pop("_id")
    user_data["password"] = "new_password"
    user_data["user_name"] = str(uuid4())
    user_data["id"] = str(user_with_goals.id)
    response = await test_client.put("user/me", json=user_data)

    assert response.status_code == 401


@pytest.mark.usefixtures("user_no_goals")
async def test_forgot_password(user_data, test_client):
    reset_info = {
        "user_name": user_data["user_name"],
        "security_question_answer": user_data["security_question_answer"],
        "new_password": "new",
    }

    response = await test_client.patch("user/forgot-password", json=reset_info)

    assert response.status_code == 200


@pytest.mark.usefixtures("user_no_goals")
async def test_forgot_password_wrong_answer(user_data, test_client):
    reset_info = {
        "user_name": user_data["user_name"],
        "security_question_answer": "bad",
        "new_password": "new",
    }

    response = await test_client.patch("user/forgot-password", json=reset_info)

    assert response.status_code == 400


@pytest.mark.usefixtures("user_no_goals")
async def test_forgot_password_not_found(user_data, test_client):
    reset_info = {
        "user_name": "unknown",
        "security_question_answer": user_data["security_question_answer"],
        "new_password": "new",
    }

    response = await test_client.patch("user/forgot-password", json=reset_info)

    assert response.status_code == 404
