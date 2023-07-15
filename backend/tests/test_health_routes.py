import pytest
from bson import ObjectId
from httpx import AsyncClient
from motor.motor_asyncio import AsyncIOMotorClient

from app.core.security import create_access_token


@pytest.fixture
async def test_client_bad_db(superuser_token_headers):
    from app.api.deps import get_db_client
    from app.core.config import config
    from app.main import app

    def get_db_client_override():
        return AsyncIOMotorClient(
            host="bad",
            username=config.mongo_initdb_root_username,
            password=config.mongo_initdb_root_password,
            port=config.mongo_port,
            serverSelectionTimeoutMS=100,
        )

    app.dependency_overrides[get_db_client] = get_db_client_override

    async with AsyncClient(
        app=app, base_url=f"http://127.0.0.1{config.V1_API_PREFIX}", headers=superuser_token_headers
    ) as client:
        yield client

    app.dependency_overrides = {}


async def test_health(test_client, superuser_token_headers):
    result = await test_client.get("health", headers=superuser_token_headers)

    assert result.status_code == 200
    assert result.json()["db"] == "healthy"


async def test_health_unhealthy(test_client_bad_db, superuser_token_headers):
    result = await test_client_bad_db.get("health", headers=superuser_token_headers)

    assert result.status_code == 200
    assert result.json()["db"] == "unhealthy"


async def test_health_not_authenticated(test_client):
    result = await test_client.get("health")

    assert result.status_code == 401


async def test_health_invalid_token(test_client):
    """This is here to test an invalid admin token."""
    bad_header = {"Authorization": "Bearer bad"}
    response = await test_client.get("health", headers=bad_header)
    assert response.status_code == 403
    assert response.json()["detail"] == "Could not validate credentials"


async def test_health_token_user_not_found(test_client):
    """This is here to test an admin token where the user isn't found."""
    bad_header = {"Authorization": f"Bearer {create_access_token(str(ObjectId()))}"}
    response = await test_client.get("health", headers=bad_header)
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"
