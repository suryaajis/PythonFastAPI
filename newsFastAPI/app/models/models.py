from .base_model import BaseModel
from sqlalchemy import Column, String, Boolean

class Post(BaseModel):
  __tablename__ = "posts"
  
  title = Column(String, nullable=False)
  content = Column(String, nullable=False)
  published = Column(Boolean, default=True, nullable=True)