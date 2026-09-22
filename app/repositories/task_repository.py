from pathlib import Path
from typing import Any

from app.repositories.link_repository import JsonLinkRepository

class TaskRepository:
  def __init__(self, path:Path)-> None:
    self.storage = JsonLinkRepository(path)

  def load_all(self) -> list[dict[str,Any]]:
    return self.storage.load_all()

  def save_all(self, tasks:list[dict[str,Any]])-> None:
    self.storage.save_all(tasks)
