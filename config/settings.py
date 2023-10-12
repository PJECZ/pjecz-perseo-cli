"""
Config - Settings  /home/guivaloz/Downloads/NOMINAS
"""
from datetime import date
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings"""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    explotacion_base_dir: str
    fecha: date = date.today()


@lru_cache()
def get_settings() -> Settings:
    """Obtiene la configuracion"""
    return Settings()
