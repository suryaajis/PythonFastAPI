from fastapi import FastAPI
from . import router_manual
from . import models
from .config import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
  return {"Hello": "Python"}


# app.include_router(router_manual.router)