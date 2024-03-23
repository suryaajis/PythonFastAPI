from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
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

