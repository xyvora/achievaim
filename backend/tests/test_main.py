from httpx import AsyncClient

from app.main import app


async def test_index():
    async with AsyncClient(app=app) as client:
        response = await client.get("http://127.0.0.1/")

    assert "<title>AchievAIm</title>" in response.text
