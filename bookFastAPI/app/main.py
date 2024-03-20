from fastapi import FastAPI
from config import engine
import model
import router

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
  return {"Hello": "Python"}

app.include_router(router.router, prefix="/book", tags=["book"])