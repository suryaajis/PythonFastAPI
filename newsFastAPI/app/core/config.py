from dotenv import load_dotenv
from sqlalchemy import create_engine, orm
from sqlalchemy.ext.declarative import declarative_base, as_declarative, declared_attr
from sqlalchemy.orm import sessionmaker
from typing import Any
import os

load_dotenv()
HOST = os.environ.get("DB_HOST")
PORT = os.environ.get("DB_PORT")
DB = os.environ.get("DB_DATABASE")
USER = os.environ.get("DB_USERNAME")
PASS = os.environ.get("DB_PASSWORD")
  
# ORM CONFIG DATABASE
# Use ORM we must declare models with create models for table on Database
DATABASE_URL = f"postgresql://{USER}:{PASS}@{HOST}:{PORT}/{DB}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
  db = SessionLocal()
  try: 
    yield db
  finally:
    db.close()

"""
@as_declarative()
class BaseModel:
  id: Any
  __name__: str

  # Generate __tablename__ automatically
  @declared_attr
  def __tablename__(cls) -> str:
    return cls.__name__.lower()
  
class Database:
  def __init__(self, db_url: str) -> None:
    self._engine = create_engine(db_url, echo=True)
    self._session_factory = orm.scoped_session(
      orm.sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=self._engine,
      ),
    )

  def create_database(self) -> None:
    BaseModel.metadata.create_all(self._engine)

  def get_db():
    db = SessionLocal()
    try: 
      yield db
    finally:
      db.close()
"""