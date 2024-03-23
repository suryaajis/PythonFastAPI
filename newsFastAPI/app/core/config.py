from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

load_dotenv()
HOST = os.environ.get("DB_HOST", "localhost")
PORT = os.environ.get("DB_PORT", "5432")
DB = os.environ.get("DB_DATABASE", "news_db")
USER = os.environ.get("DB_USERNAME", "postgres")
PASS = os.environ.get("DB_PASSWORD", "postgres")

JWT_SECRET = os.environ.get("JWT_SECRET", "SECRET_KEY")
  
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