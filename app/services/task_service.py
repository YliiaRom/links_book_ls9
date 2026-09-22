from typing import Any
from uuid import UUID, uuid4

from app.models.notes import TaskCreate
from app.repositories.task_repository import TaskRepository

class TaskService:
  def __init__(self, repository:TaskRepository)-> None:
    self.repository = repository

  def list_tasks(self)->list[dict[str,Any]]:
    return self.repository.load_all()

  def create_task(self,payload:TaskCreate)->dict[str,Any]:
    tasks = self.repository.load_all()

    task ={
      "id": str(uuid4()),
      **payload.model_dump(mode="json"),

    }

    tasks.append(task)

    self.repository.save_all(tasks)

    return task


  
  def delete_task(self,task_id: UUID)->None:

    tasks = self.repository.load_all()

    tasks =[task for task in tasks if task["id"] != str(task_id)]

    self.repository.save_all(tasks)

  
