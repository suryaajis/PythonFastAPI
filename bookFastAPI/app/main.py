from fastapi import FastAPI, Depends
from config import engine
from auth import AuthHandler
import model
import router

model.Base.metadata.create_all(bind=engine)

app = FastAPI()
auth_handler = AuthHandler()

@app.get("/")
def read_root():
  return {"Hello": "Python"}

@app.get('/protected')
def protected(username=Depends(auth_handler.auth_wrapper)):
    return { 'name': username }

app.include_router(router.router)