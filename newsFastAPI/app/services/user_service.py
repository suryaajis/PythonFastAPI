from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from ..schemas.user_schema import UserLoginRequest, UserRequest
from ..models.models import UserModel
from ..core.security import AuthHandler

auth_handler = AuthHandler()

# Auth User Services
def register_user(db:Session, request: UserRequest):
  if db.query(UserModel).filter(UserModel.username == request.username).first():
    raise HTTPException(status_code=400, detail='Username is taken')
  
  hashed_pass = auth_handler.get_password_hash(request.password)
  new_user = UserModel(email= request.email, username=request.username, password=hashed_pass)
  
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user

def login_user(db:Session, request: UserLoginRequest):
  user = db.query(UserModel).filter(UserModel.email == request.email).first()
  
  if user is None or not auth_handler.verify_password(request.password, user.password):
    raise HTTPException(status_code=401, detail='Invalid username and/or password')
    
  token = auth_handler.encode_token(user.id)
  return {"access_token": token, "token_type": "bearer"}


# User Services
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