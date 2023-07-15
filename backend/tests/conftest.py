import asyncio
from copy import deepcopy
from uuid import uuid4

import pytest
from httpx import AsyncClient
from pymongo.errors import OperationFailure

from app.core.config import config
from app.core.security import get_password_hash
from app.db import init_db
from app.main import app
from app.models.user import User


@pytest.fixture(scope="session", autouse=True)
async def initialize_db():
    try:
        await init_db()
    except OperationFailure:  # init_db already ran
        pass


@pytest.fixture(autouse=True)
async def clear_db():
    yield
    await User.delete_all()


@pytest.fixture(scope="session", autouse=True)
def event_loop():
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def test_client():
    async with AsyncClient(app=app, base_url=f"http://127.0.0.1{config.V1_API_PREFIX}") as client:
        yield client


@pytest.fixture
def user_data():
    return {
        "_id": "649a39c599ef045345c94afc",
        "user_name": "immauser",
        "hashed_password": get_password_hash("test_password"),
        "goals": [
            {
                "id": str(uuid4()),
                "name": "Goal 1",
                "duration": 5,
                "days_of_week": {
                    "monday": False,
                    "tuesday": False,
                    "wednesday": True,
                    "thursday": False,
                    "friday": False,
                    "saturday": False,
                    "sunday": False,
                },
                "repeats_every": "week",
                "progress": 41.0,
            },
            {
                "id": str(uuid4()),
                "name": "Goal 2",
                "duration": 2,
                "days_of_week": {
                    "monday": True,
                    "tuesday": True,
                    "wednesday": False,
                    "thursday": True,
                    "friday": True,
                    "saturday": True,
                    "sunday": True,
                },
                "repeats_every": "day",
                "progress": 42.0,
            },
        ],
    }


@pytest.fixture
async def user_with_goals(user_data):
    return await User(**user_data).insert()


@pytest.fixture
async def user_no_goals(user_data):
    user_data_copy = deepcopy(user_data)
    user_data_copy["user_name"] = "immauser"
    user_data_copy["goals"] = None
    return await User(**user_data_copy).insert()


@pytest.fixture
async def admin_user():
    return await User(
        user_name="admin", hashed_password=get_password_hash("test_password"), is_admin=True
    ).insert()


@pytest.fixture
async def superuser_token_headers(test_client, admin_user):
    login_data = {
        "username": admin_user.user_name,
        "password": "test_password",
    }
    response = await test_client.post("/login/access-token", data=login_data)
    tokens = response.json()
    a_token = tokens["access_token"]
    headers = {"Authorization": f"Bearer {a_token}"}
    return headers


@pytest.fixture
async def user_token_headers(test_client):
    login_data = {
        "username": "immauser",
        "password": "test_password",
    }
    response = await test_client.post("/login/access-token", data=login_data)
    tokens = response.json()
    a_token = tokens["access_token"]
    headers = {"Authorization": f"Bearer {a_token}"}
    return headers
