import asyncio

import pytest
from httpx import AsyncClient

from app.core.config import config
from app.core.security import get_password_hash
from app.main import app
from app.models.user import User


@pytest.fixture(autouse=True)
async def clear_db():
    yield
    students = await User.find_all().to_list()

    for student in students:
        await student.delete()

    goals = await User.find_all().to_list()

    for goal in goals:
        await goal.delete()


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
                "name": "Goal 1",
                "duration": 5,
                "daysOfWeek": {
                    "monday": False,
                    "tuesday": False,
                    "wednesday": True,
                    "thursday": False,
                    "friday": False,
                    "saturday": False,
                    "sunday": False,
                },
                "repeatsEvery": "day",
                "progress": 41.0,
            }
        ],
    }


@pytest.fixture
async def user(user_data):
    return await User(**user_data).insert()
