from .config import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

class Post(Base):
  __tablename__ = "posts"
  
  id = Column(Integer, primary_key=True, nullable=False)
  title = Column(String, nullable=False)
  content = Column(String, nullable=False)
  published = Column(Boolean, default=True, nullable=True)
  created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))