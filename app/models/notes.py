from pydantic import BaseModel,ConfigDict, Field, field_validator

from uuid import UUID


class TaskCreate(BaseModel):

  task: str = Field(max_length=1000, min_length=1, examples=['task'])

  @field_validator("task")
  @classmethod
  def normalize_task(cls, value:str)-> str:
    normalize = value.strip()
    if not normalize:
      raise ValueError("поле task не може бути порожнім")
    return normalize

class TaskUpdate(BaseModel):

  task: str| None = Field( default= None, max_length=1000, min_length=1)

  @field_validator("task")
  @classmethod
  def normalize_task(cls, value:str)-> str| None:
    if value is None:
      return None
    normalize = value.strip()
    if not normalize:
      raise ValueError("поле task не може бути порожнім")
    return normalize

class NoteTaskOut(TaskCreate):
  model_config = ConfigDict(from_attributes=True)
  id:UUID