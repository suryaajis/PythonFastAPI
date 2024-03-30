from fastapi import FastAPI
from .models import models
from .core.config import engine
from .routers import post_router, user_router, vote_router

models.BaseModel.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
  return {"Hello": "Python"}

app.include_router(post_router.router)
app.include_router(user_router.router)
app.include_router(vote_router.router)
# app.include_router(manual_router.router)