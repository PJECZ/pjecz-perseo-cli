"""
Config - Settings
"""
from datetime import date
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings"""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    EXPLOTACION_BASE_DIR: str
    FECHA: date = date.today()
    SALT: str
    SQLALCHEMY_DATABASE_URI: str


@lru_cache()
def get_settings() -> Settings:
    """Obtiene la configuracion"""
    return Settings()
