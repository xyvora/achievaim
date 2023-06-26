import asyncio
import os
from unittest.mock import patch

import pytest
from httpx import AsyncClient

from app.models.goals import Goal


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
        from app.config import V1_API_PREFIX
        from app.db import init_db
        from app.main import app

        await init_db()

        async with AsyncClient(app=app, base_url=f"http://localhost{V1_API_PREFIX}") as client:
            yield client
