from enum import Enum
from uuid import UUID


from pydantic import BaseModel, ConfigDict, Field,field_validator

class Themes(str,Enum):
  py ="py"
  react="react"
  js="js"
  py_bk="py_bk"


class ColorDecorator(str, Enum):
  red = "red"
  green="green"
  blue= 'blue'
  black='black'
  yellow='yellow'

def normalizer(val):
  normalize_val = val.strip()
  if not normalize_val:
    raise ValueError(f"Поле {val} не може бути порожнім")
  return normalize_val

class LinksBookCreator(BaseModel):
  school: str = Field(min_length=2, max_length=300, examples=['Frilanser by life'])
  themes:Themes
  title:str = Field(min_length=1, max_length=1000, examples=['назва'])
  title_link:str = Field( min_length=1, max_length=1000, examples=["Посилaння на тему"])
  description:str = Field(min_length=0, max_length=1000, examples=['короткий опис'])

  links:str = Field(min_length=3, max_length=1000)

  number_lection:int = Field(gt=0,le=100,examples=[1])
  time_lection:str = Field(pattern=r"^\d{2}\.\d{2}$", examples=['02.10'])

  sub_description:str | None = Field(min_length=0, max_length=1000, examples=['помітки для себе'])
  color_decorator:ColorDecorator


  @field_validator(
    "title",
    
     "school",
     "title_link",
    "description",
    "links",
    "sub_description",)
  @classmethod
  def normalize_val(cls,val:str)->str:
      return normalizer(val)


class LinksBookUpdate(BaseModel):
  school: str| None = Field(default = None, min_length=2, max_length=300)
  themes:Themes | None = None
  title:str | None = Field(default = None, min_length=1, max_length=1000)
  title_link:str | None = Field(default = None, min_length=1, max_length=1000)
  description:str | None = Field(default = None, min_length=0, max_length=1000)

  links:str| None = Field(default = None, min_length=3, max_length=1000)

  number_lection:int| None = Field(default = None, gt=0)
  time_lection:str| None = Field(default = None, pattern=r"^\d{2}\.\d{2}$")

  sub_description:str | None = Field(default = None, min_length=0, max_length=1000)
  color_decorator:ColorDecorator | None = None


  @field_validator(
    "title",
    "school",
    "title_link",
    "description",
    "links",
    "sub_description",)
  @classmethod
  def normalize_val(cls,val:str)->str:
      return normalizer(val)


class LinkOut(LinksBookCreator):
    model_config=ConfigDict(from_attributes=True)
    id:UUID



