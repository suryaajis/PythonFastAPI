from .base_model import BaseModel
from sqlalchemy import Column, String, Boolean

class PostModel(BaseModel):
  __tablename__ = "posts"
  
  title = Column(String, nullable=False)
  content = Column(String, nullable=False)
  published = Column(Boolean, default=True, nullable=True)
  
class UserModel(BaseModel):
  __tablename__ = "users"
  
  email = Column(String, nullable=False, unique=True)
  username = Column(String, nullable=False)
  password = Column(String, nullable=False)
  is_active = Column(Boolean, default=True)