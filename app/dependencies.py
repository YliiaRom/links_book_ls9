from typing import Annotated
from fastapi import Depends

from app.core.config import Settings, get_settings
from app.repositories.link_repository import JsonLinkRepository
from app.services.link_service import LinkService
from app.repositories.task_repository import TaskRepository
from app.services.task_service import TaskService


SettingsDependency = Annotated[Settings,Depends(get_settings)]

def get_link_services(settings: SettingsDependency)->LinkService:
  return LinkService(JsonLinkRepository(settings.data_file))

def get_task_repository(settings:SettingsDependency)->TaskRepository:
  return TaskRepository(settings.tasks_file)

def get_task_service(settings:SettingsDependency)-> TaskService:
  return TaskService(TaskRepository(settings.tasks_file))