from pydantic import BaseModel, EmailStr
from .base_schema import ModelBaseInfo



class BaseUser(BaseModel):
  email = EmailStr
  username = str
  password = str
  
class User(ModelBaseInfo, BaseUser):
  ...