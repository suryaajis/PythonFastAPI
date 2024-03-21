from sqlalchemy import Column, Integer, String
from config import Base


class Book(Base):
  __tablename__ = 'book'
  
  id=Column(Integer, primary_key=True)
  title=Column(String)
  description=Column(String)
  
class User(Base):
  __tablename__ = 'user'
  
  id=Column(Integer, primary_key=True)
  username=Column(String)
  password=Column(String)