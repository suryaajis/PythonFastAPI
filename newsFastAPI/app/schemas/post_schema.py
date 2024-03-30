from pydantic import BaseModel
from .base_schema import ModelBaseInfo
from .user_schema import UserResponse

class BasePost(BaseModel):
  title: str
  content: str
  published: bool = True
  
  class Config:
    orm_mode: True
  
class PostSchema(ModelBaseInfo, BasePost):
    ...
    user_id: int
    user: UserResponse
    
    class Config:
      orm_mode: True
    
class PostRequest(BasePost):
  pass

class PostResponse(BasePost):
  ...