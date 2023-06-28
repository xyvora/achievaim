import logging
from typing import Final

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    mongo_initdb_database: str = Field(..., env="MONGO_INITDB_DATABASE")
    mongo_initdb_root_username: str = Field(..., env="MONGO_INITDB_ROOT_USERNAME")
    mongo_initdb_root_password: str = Field(..., env="MONGO_INITDB_ROOT_PASSWORD")
    mongo_host: str = Field(..., env="MONGO_HOST")
    mongo_port: int = Field(27017, env="MONGO_PORT")
    log_level: int = logging.INFO


V1_API_PREFIX: Final[str] = "/api/v1"
config = Settings()  # type: ignore[call-arg]
