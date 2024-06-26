from pydantic import BaseModel, EmailStr
from .base_schema import ModelBaseInfo

class BaseUser(BaseModel):
  email: EmailStr
  username: str
  password: str
  is_active: bool = True
  
class UserSchema(ModelBaseInfo, BaseUser):
  ...
  
class UserRequest(BaseUser):
  pass

class UserDisableRequest(BaseModel):
  is_active: bool
  
class UserLoginRequest(BaseModel):
  email: EmailStr
  password: str
  
class UserResponse(BaseModel):
  id: int
  email: str
  
  class Config:
    orm_mode = True