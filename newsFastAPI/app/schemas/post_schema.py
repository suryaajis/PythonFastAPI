from pydantic import BaseModel
from .base_schema import ModelBaseInfo

class BasePost(BaseModel):
  title: str
  content: str
  published: bool = True
  
  class Config:
    orm_mode: True
  
class PostSchema(ModelBaseInfo, BasePost):
    ...
    
class PostRequest(BasePost):
  pass