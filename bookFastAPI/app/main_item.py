from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    item_id: int 
    name: str
    price: float
    brand: Optional[str] = None
    
class UpdatedItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

database = {}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/get-item")
def read_item():
    return database

@app.get("/get-item/{item_id}")
def read_item_by_id(item_id: int):
    return database[item_id]

@app.post("/create-item")
def create_item(item: Item):
    if item.item_id in database:
        return {"Error": "Item already exists."}
    database[item.item_id] = item
    return item

@app.put("/update-item/{item_id}")
def update_item(item_id, item: Item):
    if item_id not in database:
        return {"Error": "Item ID does not exists."}
    
    