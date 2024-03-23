from pydantic import BaseModel
from .base_schema import FindBase, ModelBaseInfo, SearchOptions

class BasePost(BaseModel):
  title: str
  content: str
  published: bool = True
  
  class Config:
    orm_mode: True
  
class Post(ModelBaseInfo, BasePost):
    ...