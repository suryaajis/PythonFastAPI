from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import psycopg2
import time
import os

load_dotenv()
HOST = os.environ.get("DB_HOST")
PORT = os.environ.get("DB_PORT")
DB = os.environ.get("DB_DATABASE")
USER = os.environ.get("DB_USERNAME")
PASS = os.environ.get("DB_PASSWORD")

# MANUAL CONFIG DATABASE
# create database, table, column and row manual on GUI

while True:  
  try:
    conn = psycopg2.connect(host=HOST, database=DB, user=USER, password=PASS, cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    print("Database connection was succesfull!")
    break
  except Exception as error:
    print("Connecting to database failed")
    print(f"Error: {error}")
    time.sleep(3)