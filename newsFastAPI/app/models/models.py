from .base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey

class PostModel(BaseModel):
  __tablename__ = "posts"
  
  title = Column(String, nullable=False)
  content = Column(String, nullable=False)
  published = Column(Boolean, default=True, nullable=True)
  user_id = Column(Integer, ForeignKey("users.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
  user = relationship("UserModel")
  
class UserModel(BaseModel):
  __tablename__ = "users"
  
  email = Column(String, nullable=False, unique=True)
  username = Column(String, nullable=False)
  password = Column(String, nullable=False)
  is_active = Column(Boolean, default=True)
  
class VoteModel(BaseModel):
  __tablename__ = "votes"
  
  user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
  post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), nullable=False)
  is_voted = Column(Boolean, default=False)
  user = relationship("UserModel")
  post = relationship("PostModel")