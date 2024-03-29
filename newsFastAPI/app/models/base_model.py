from datetime import datetime
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.sql.expression import text
from ..core.config import Base

class BaseModel(Base):
  __abstract__ = True
  
  id = Column(Integer, primary_key=True, index=True, nullable=False)
  created_at = Column(DateTime, default=datetime.utcnow)
  updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
