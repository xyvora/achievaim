import logging
import secrets
from typing import Final

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    V1_API_PREFIX: Final[str] = "/api/v1"

    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: Final[int] = 60 * 24 * 8
    SECRET_KEY: Final[str] = secrets.token_urlsafe(32)

    mongo_initdb_database: str = "mongo_test"
    mongo_initdb_root_username: str = "mongo"
    mongo_initdb_root_password: str = "mongo_password"
    mongo_host: str = "mongodb://127.0.0.1"
    mongo_port: int = 27017
    log_level: int = logging.INFO
    openai_api_key: str = "key"
    openai_organization: str | None = None
    openai_url: str = "https://api.openai.com/v1/chat/completions"
    # model_config = SettingsConfigDict(case_sensitive=True)


config = Settings()  # type: ignore
