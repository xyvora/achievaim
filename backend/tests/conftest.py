import asyncio
import os
from unittest.mock import patch

import pytest
from httpx import AsyncClient

from app.models.goals import Goal


@pytest.fixture(autouse=True, scope="session")
def mock_env():
    with patch.dict(
        os.environ,
        {
            "MONGO_INITDB_DATABASE": "smartgoalpt_test",
            "MONGO_INITDB_ROOT_USERNAME": "mongo",
            "MONGO_INITDB_ROOT_PASSWORD": "mongo_password",
            "MONGO_PORT": "27017",
            "MONGO_HOST": "localhost",
        },
        clear=True,
    ):
        yield


@pytest.fixture(autouse=True)
async def clear_db():
    yield
    students = await Goal.find_all().to_list()

    for student in students:
        await student.delete()

    goals = await Goal.find_all().to_list()

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
    with patch.dict(
        os.environ,
        {
            "MONGO_INITDB_DATABASE": "smartgoalpt",
            "MONGO_INITDB_ROOT_USERNAME": "mongo",
            "MONGO_INITDB_ROOT_PASSWORD": "mongo_password",
            "MONGO_PORT": "27017",
            "MONGO_HOST": "localhost",
        },
        clear=True,
    ):
        from app.core.config import config
        from app.db import init_db
        from app.main import app

        await init_db()

        async with AsyncClient(
            app=app, base_url=f"http://127.0.0.1{config.V1_API_PREFIX}"
        ) as client:
            yield client


@pytest.fixture
def goal_data():
    return {
        "_id": "649a39c599ef045345c94afc",
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


@pytest.fixture
async def goal(goal_data):
    goal = await Goal(**goal_data).insert()
    return goal
