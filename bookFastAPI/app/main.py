from fastapi import FastAPI, Depends, BackgroundTasks
from .config import engine
from .auth import AuthHandler
from .helper.mailer import send_email
from .schemas import MailBody
from . import model
from . import router

model.Base.metadata.create_all(bind=engine)

app = FastAPI()
auth_handler = AuthHandler()

@app.get("/")
def read_root():
  return {"Hello": "Python"}

@app.get('/protected')
def protected(username=Depends(auth_handler.auth_wrapper)):
    return { 'name': username }

@app.post("/send-email")
def schedule_email(req:MailBody, tasks:BackgroundTasks):
  data = req.dict()
  tasks.add_task(send_email, data)
  return {"status": 200, "message": "email has been scheduled"}

app.include_router(router.router)