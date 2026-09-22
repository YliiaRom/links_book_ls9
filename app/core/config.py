from functools import lru_cache
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
  app_name:str = "Links Api with Romanenko Yuliia"
  data_file:Path = Path('data/links.json')
  tasks_file: Path = Path("data/tasks.json")
  debug: bool = False

  model_config= SettingsConfigDict(
    env_file=".env",
    env_file_encoding="utf-8",
    env_prefix="APP_",
    extra="ignore",
  )

@lru_cache
def get_settings()->Settings:
  return Settings()