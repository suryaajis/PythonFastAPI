from fastapi import FastAPI
from .config import cursor

app = FastAPI()

@app.get("/")
def root():
  return {"Hello": "Python"}

@app.get("/posts")
def read_posts():
  cursor.execute("""SELECT * FROM posts """)
  posts = cursor.fetchall()
  return {"data": posts}