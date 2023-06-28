from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.config import config
from app.models.goals import Goal

db_client = AsyncIOMotorClient(
    host=config.mongo_host,
    username=config.mongo_initdb_root_username,
    password=config.mongo_initdb_root_password,
    port=config.mongo_port,
)


async def init_db() -> None:
    await init_beanie(database=db_client.db_name, document_models=[Goal])  # type: ignore[arg-type]
