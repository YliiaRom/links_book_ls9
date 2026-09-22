from typing import Annotated
from fastapi import APIRouter, Depends, status,Form
from fastapi.responses import RedirectResponse
from uuid import UUID


from app.dependencies import get_task_service
from app.models.notes import NoteTaskOut, TaskCreate
from app.services.task_service import TaskService

router = APIRouter(prefix="/notes",tags=['notes'])

TaskServiceDependency = Annotated[
  TaskService, Depends(get_task_service),
]
@router.get("", response_model=list[NoteTaskOut])
def list_tasks(service:TaskServiceDependency):
  return service.list_tasks()

@router.post("", response_model=NoteTaskOut, status_code=status.HTTP_201_CREATED)
def create_task(
  payload:TaskCreate,
  service: TaskServiceDependency,
):
  return service.create_task(payload)

@router.post("/add")
def create_new_task(task:str= Form(...), service:TaskServiceDependency = None):
  payload = TaskCreate(task=task)

  service.create_task(payload)

  return RedirectResponse("/notes-page", status_code=303)

@router.post("/{task_id}/delete")
def delete_task(
    task_id: UUID,
    service: TaskServiceDependency,
):
    service.delete_task(task_id)

    return RedirectResponse(
        "/notes-page",
        status_code=303,
    )
