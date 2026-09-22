from typing import Annotated

from fastapi import APIRouter, Request, Depends
from fastapi.templating import (  Jinja2Templates, )


from app.dependencies import get_link_services, get_task_service
from app.services.link_service import LinkService

from app.services.task_service import TaskService

router = APIRouter()

templates = Jinja2Templates(directory="templates")

LinkServiceDependency = Annotated[LinkService, Depends(get_link_services)]
TaskServiceDependency = Annotated[
    TaskService,
    Depends(get_task_service),
]

fakeList = [
    {
        "school": "Fr/bk",
        "themes": "py",
        "title": "Python",
        "description": "Основи Python та робота з даними",
        "links": "https://www.python.org/",
        "number_lection": 1,
        "time_lection": "02.10",
        "sub_description": "Повторити змінні та типи даних",
        "color_decorator": "blue",
    },
    {
        "school": "Fr",
        "themes": "py",
        "title": "Функції в Python",
        "description": "Створення та використання функцій",
        "links": "https://docs.python.org/3/tutorial/controlflow.html#defining-functions",
        "number_lection": 2,
        "time_lection": "15.30",
        "sub_description": "Розібрати параметри та return",
        "color_decorator": "green",
    },
    {
        "school": "Fr",
        "themes": "js",
        "title": "JavaScript",
        "description": "Основи JavaScript та робота з DOM",
        "links": "https://developer.mozilla.org/en-US/docs/Web/JavaScript",
        "number_lection": 3,
        "time_lection": "08.45",
        "sub_description": "Повторити querySelector та events",
        "color_decorator": "yellow",
    },
    {
        "school": "Fr",
        "themes": "react",
        "title": "React",
        "description": "Компоненти та props у React",
        "links": "https://react.dev/",
        "number_lection": 4,
        "time_lection": "21.15",
        "sub_description": "Повторити передачу props",
        "color_decorator": "red",
    },
]

@router.get('/')
def read_root(request:Request,
              service:LinkServiceDependency):
  
  links =service.list_links()

  return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={"links":links, 'title': 'Links---Book'}
  )
@router.get("/notes-page")
def notes_page(request:Request, service: TaskServiceDependency):
  tasks = service.list_tasks()

  return templates.TemplateResponse(
    request=request,
    name="notes.html",
    context={
      "tasks":tasks,
      "title": "Notes"
    }
  )