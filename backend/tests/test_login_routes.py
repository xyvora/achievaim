from uuid import uuid4

import pytest
from bson import ObjectId

from app.core.security import create_access_token
from app.models.user import UserUpdate
from app.services.user_service import update_user


@pytest.mark.usefixtures("user_with_goals")
async def test_get_access_token(test_client):
    login_data = {
        "username": "immauser",
        "password": "test_password",
    }
    response = await test_client.post("login/access-token", data=login_data)
    tokens = response.json()
    assert response.status_code == 200
    assert "access_token" in tokens
    assert tokens["access_token"]


async def test_get_access_token_user_not_found(test_client):
    login_data = {
        "username": "immauser",
        "password": "test_password",
    }
    response = await test_client.post("login/access-token", data=login_data)
    assert response.status_code == 400
    assert "Incorrect user name or password" == response.json()["detail"]


async def test_get_access_token_inactivate_user(test_client, user_with_goals):
    response = await update_user(
        UserUpdate(
            id=user_with_goals.id,
            user_name=user_with_goals.user_name,
            password="test_password",
            is_active=False,
            is_admin=user_with_goals.is_admin,
        ),
    )
    response = await user_with_goals.update({"$set": update_user})
    login_data = {
        "username": user_with_goals.user_name,
        "password": "test_password",
    }
    response = await test_client.post("login/access-token", data=login_data)
    assert response.status_code == 400
    assert "Inactive user" == response.json()["detail"]


@pytest.mark.usefixtures("user_with_goals")
async def test_get_access_token_bad_password(test_client):
    login_data = {
        "username": "immauser",
        "password": str(uuid4()),
    }
    response = await test_client.post("login/access-token", data=login_data)
    assert response.status_code == 400
    assert "Incorrect user name or password" == response.json()["detail"]


async def test_use_access_token(test_client, superuser_token_headers):
    response = await test_client.post("login/test-token", headers=superuser_token_headers)
    assert response.status_code == 200
    assert "id" in response.json()


async def test_use_access_token_invalid_token(test_client):
    bad_header = {"Authorization": "Bearer bad"}
    response = await test_client.post("login/test-token", headers=bad_header)
    assert response.status_code == 403
    assert response.json()["detail"] == "Could not validate credentials"


async def test_use_access_token_user_not_found(test_client):
    bad_header = {"Authorization": f"Bearer {create_access_token(str(ObjectId()))}"}
    response = await test_client.post("login/test-token", headers=bad_header)
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"
