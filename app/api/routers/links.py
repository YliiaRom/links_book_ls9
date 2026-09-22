from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, Response,status,Form

from fastapi.responses import RedirectResponse

from app.dependencies import get_link_services
from app.models.links import Themes,LinksBookUpdate,LinksBookCreator,LinkOut,ColorDecorator
from app.repositories.link_repository import StorageError
from app.services.link_service import LinksNotFoundError, LinkService




router = APIRouter(prefix="/links", tags=["links"])




LinkServiceDependency= Annotated[LinkService, Depends(get_link_services)]

ThemesQuery=Annotated[Themes | None, Query(description="Фільтр посилань за мовою програмування")]

def raise_storage_error(error:StorageError)-> None:
  raise HTTPException(status_code=500,detail="Помилка локального сховища") from error


@router.get('', response_model=list[LinkOut])
def list_links(service:LinkServiceDependency, themes:ThemesQuery = None)-> list[dict]:
  try:
    return service.list_links(themes.value if themes else None)

  except StorageError as error:
    raise_storage_error(error)

@router.get("/{link_id}", response_model=LinkOut)
def get_links_by_id(link_id:UUID, service:LinkServiceDependency) -> dict:
  try:
    return service.get_link(link_id)

  except LinksNotFoundError as error:
    raise HTTPException(status_code=404, detail="Посилання не знайдено") from error

  except StorageError as error:
    raise_storage_error(error)

@router.post("",response_model=LinkOut, status_code=status.HTTP_201_CREATED)
def create_link(payload: LinksBookCreator,service:LinkServiceDependency)-> dict:
  try:
    return service.create_link(payload)
  except StorageError as error:
    raise_storage_error(error)

@router.post("/add")
def create_new_link(service: LinkServiceDependency, school:str= Form(...), themes:Themes = Form(...),title:str= Form(...),title_link:str =Form(...),description:str = Form(...), links:str = Form(...), number_lection:int= Form(...), time_lection:str= Form(...), sub_description:str | None= Form(None), color_decorator:ColorDecorator = Form(...)) -> RedirectResponse:
      try:
            payload = LinksBookCreator(
            school=school,
            themes=themes,
            title=title,
            title_link=title_link,
            description=description,
            links=links,
            number_lection=number_lection,
            time_lection=time_lection,
            sub_description=sub_description,
            color_decorator=color_decorator,
        )
            
            service.create_link(payload)

            return RedirectResponse("/", status_code=303)
      
      except StorageError as error:

        raise_storage_error(error)

  #   school: str| None = Field(default = None, min_length=2, max_length=300)
  # themes:Themes | None = None
  # title:str | None = Field(default = None, min_length=1, max_length=1000)
  # description:str | None = Field(default = None, min_length=0, max_length=1000)

  # links:str| None = Field(default = None, min_length=3, max_length=1000)

  # number_lection:int| None = Field(default = None, gt=0,le=4)
  # time_lection:str| None = Field(default = None, pattern=r"^\d{2}.\d{2}$")

  # sub_description:str | None = Field(default = None, min_length=0, max_length=1000)
  # color_decorator:ColorDecorator | None = None

@router.patch('/{link_id}', response_model=LinkOut)
def update_link(link_id: UUID, payload:LinksBookUpdate, service: LinkServiceDependency)-> dict:
  try:
    return service.update_link(link_id,payload)
  except LinksNotFoundError as error:
    raise HTTPException(status_code=404,detail="Посилання не знайдено") from error
  except StorageError as error:
    raise_storage_error(error)

@router.delete("/{link_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_link(link_id:UUID, service: LinkServiceDependency) -> Response:
  try:
    service.delete_link(link_id)

  except LinksNotFoundError as error:
    raise HTTPException(status_code=404, detail="Посилання не знайдено") from error
  except StorageError as error:
    raise_storage_error(error)
  return Response(status_code=status.HTTP_204_NO_CONTENT)



  