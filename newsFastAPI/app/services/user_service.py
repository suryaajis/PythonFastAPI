from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from ..schemas.user_schema import UserRequest
from ..models.models import UserModel

def register_user(db:Session, req:UserRequest):
  return {}

def get_users(db:Session):
  users = db.query(UserModel).all()
  return users

def get_user_by_id(db:Session, id:int):
  user = db.query(UserModel).filter(UserModel.id == id).first()
  
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User ID {id} not found")
  
  return user

def disable_user(db:Session, id:int, is_active:bool):
  user = get_user_by_id(db, id)
  
  user.is_active = is_active
  db.commit()
  return user 