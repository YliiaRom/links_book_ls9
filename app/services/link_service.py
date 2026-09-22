
from typing import Any
from uuid import UUID, uuid4


from app.models.links import LinksBookCreator, LinksBookUpdate
from app.repositories.link_repository import JsonLinkRepository


class LinksNotFoundError(LookupError):
  pass

class LinkService:
  def __init__(self, repository:JsonLinkRepository)-> None:
    self.repository = repository

  def list_links(self, themes:str|None =None)->list[dict[str, Any]]:
    links = self.repository.load_all()

    if themes is not None:
      links = [link for link in links if link["themes"]== themes]
    return sorted(links, key=lambda link:link["id"])

  def get_link(self, link_id: UUID)->dict[str,Any]:
    for link in self.repository.load_all():
      if link['id']==str(link_id):
        return link
    raise LinksNotFoundError(link_id)

  def create_link(self, payload:LinksBookCreator)->dict[str,Any]:
    links = self.repository.load_all()

    link = {"id":str(uuid4()), **payload.model_dump(mode="json")}
    links.append(link)

    self.repository.save_all(links)
    return link


  def update_link(self, link_id:UUID,payload:LinksBookUpdate)->dict[str, Any]:
    links = self.repository.load_all()

    for link in links:
      if link["id"] == str(link_id):
        link.update(payload.model_dump(exclude_unset=True, mode="json"))
        self.repository.save_all(links)

        return link

    raise LinksNotFoundError(link_id)

  def delete_link(self, link_id:UUID)->None:
    links = self.repository.load_all()

    remaining = [link for link in links if link["id"] != str(link_id)]

    if len(remaining) == len(links):
      raise LinksNotFoundError(link_id)

    self.repository.save_all(remaining)




