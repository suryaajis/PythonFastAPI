from pydantic import BaseModel
from .base_schema import ModelBaseInfo

class BasePost(BaseModel):
  title: str
  content: str
  published: bool = True
  
  
class PostSchema(ModelBaseInfo, BasePost):
    ...
    
    class Config:
      orm_mode: True
    
class PostRequest(BasePost):
  pass