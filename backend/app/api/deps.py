import logging
from typing import Annotated

from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient

from app.config import config
from app.db import db_client

logging.basicConfig(format="%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s")
logging.root.setLevel(level=config.log_level)
logger = logging


def get_db_client() -> AsyncIOMotorClient:
    return db_client


MongoClient = Annotated[AsyncIOMotorClient, Depends(get_db_client)]
