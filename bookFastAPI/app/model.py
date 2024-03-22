from sqlalchemy import Column, Integer, String
from config import Base


class Book(Base):
  __tablename__ = 'book'
  
  id=Column(Integer, primary_key=True, nullable=False)
  title=Column(String, nullable=False)
  description=Column(String, nullable=False)
  
class User(Base):
  __tablename__ = 'user'
  
  id=Column(Integer, primary_key=True, nullable=False)
  username=Column(String, unique=True, nullable=False)
  password=Column(String, nullable=False)