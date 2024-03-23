from fastapi import FastAPI
from .models import models
from .core.config import engine

models.BaseModel.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
  return {"Hello": "Python"}


# app.include_router(router_manual.router)