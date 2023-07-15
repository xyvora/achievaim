import logging
import secrets
from typing import Final

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    V1_API_PREFIX: Final[str] = "/api/v1"

    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: Final[int] = 60 * 24 * 8
    SECRET_KEY: Final[str] = Field(secrets.token_urlsafe(32), env="SECRET_KEY")

    mongo_initdb_database: str = Field("mongo_test", env="MONGO_INITDB_DATABASE")
    mongo_initdb_root_username: str = Field("mongo", env="MONGO_INITDB_ROOT_USERNAME")
    mongo_initdb_root_password: str = Field("mongo_password", env="MONGO_INITDB_ROOT_PASSWORD")
    mongo_host: str = Field("mongodb://127.0.0.1", env="MONGO_HOST")
    mongo_port: int = Field(27017, env="MONGO_PORT")
    log_level: int = Field(logging.INFO, env="LOG_LEVEL")

    class Config:
        case_sensitive = True


config = Settings()  # type: ignore
