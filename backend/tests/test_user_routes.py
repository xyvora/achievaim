from uuid import uuid4

from bson import ObjectId


async def test_create_user(test_client):
    user_data = {"userName": "arthurdent", "password": "immapassword"}
    response = await test_client.post("user/", json=user_data)
    response_json = response.json()

    assert response_json["userName"] == user_data["userName"]


async def test_create_user_duplicate(user_with_goals, test_client):
    user_data = {"userName": user_with_goals.user_name, "password": "immapassword"}
    response = await test_client.post("user/", json=user_data)

    assert response.status_code == 400


async def test_get_users(user_with_goals, test_client):
    response = await test_client.get("user/")
    response_json = response.json()

    assert len(response_json) == 1
    assert response_json[0]["userName"] == user_with_goals.user_name


async def test_get_users_no_users(test_client):
    response = await test_client.get("user/")

    assert response.status_code == 404


async def test_get_user_by_id(user_with_goals, test_client):
    response = await test_client.get(f"user/{user_with_goals.id}")
    response_json = response.json()

    assert response_json["userName"] == user_with_goals.user_name


async def test_get_user_by_id_not_found(test_client):
    response = await test_client.get(f"user/{str(ObjectId())}")

    assert response.status_code == 404


async def test_get_user_by_id_invalid_id(test_client):
    response = await test_client.get("user/bad")

    assert response.status_code == 400


async def test_get_user_by_name(user_with_goals, test_client):
    response = await test_client.get(f"user/user-name/{user_with_goals.user_name}")
    response_json = response.json()

    assert response_json["userName"] == user_with_goals.user_name


async def test_get_user_by_name_not_found(test_client):
    response = await test_client.get(f"user/user-name/{uuid4()}")

    assert response.status_code == 404


async def test_delete_user_by_id(user_with_goals, test_client):
    response = await test_client.delete(f"user/{user_with_goals.id}")
    assert response.status_code == 204

    response = await test_client.get(f"user/{user_with_goals.id}")
    assert response.status_code == 404


async def test_delete_user_by_id_not_found(test_client):
    response = await test_client.delete(f"user/{str(ObjectId())}")

    assert response.status_code == 404


async def test_delete_user_by_id_invalid_id(test_client):
    response = await test_client.delete("user/bad")

    assert response.status_code == 400


async def test_delete_user_by_user_name(user_with_goals, test_client):
    response = await test_client.delete(f"user/user-name/{user_with_goals.user_name}")
    assert response.status_code == 204

    response = await test_client.get(f"user/{user_with_goals.id}")
    assert response.status_code == 404


async def test_delete_user_by_user_name_not_found(test_client):
    response = await test_client.delete(f"user/user-name/{uuid4()}")

    assert response.status_code == 404


async def test_update_user(user_with_goals, user_data, test_client):
    user_data.pop("goals")
    user_data.pop("_id")
    user_data["password"] = "new_password"
    user_data["user_name"] = str(uuid4())
    user_data["id"] = str(user_with_goals.id)
    response = await test_client.put("user/", json=user_data)

    assert response.json()["userName"] == user_data["user_name"]


async def test_update_user_not_found(test_client):
    user_data = {"id": str(ObjectId()), "userName": "user", "password": "password"}
    response = await test_client.put("user/", json=user_data)

    assert response.status_code == 404


async def test_update_user_duplicate_user_name(test_client, user_with_goals):
    user_data = {"userName": str(uuid4), "password": "some_password"}
    response = await test_client.post("user/", json=user_data)
    assert response.status_code == 200
    user_data["id"] = response.json()["id"]
    user_data["userName"] = user_with_goals.user_name
    response = await test_client.put("user/", json=user_data)

    assert response.status_code == 400
