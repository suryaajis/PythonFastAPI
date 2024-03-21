from fastapi import HTTPException
from sqlalchemy.orm import Session
from model import Book, User
from schemas import AuthSchema, RequestBook
from auth import AuthHandler

auth_handler = AuthHandler()

# Register User
def register_user(db:Session, request: AuthSchema):
  if db.query(User).filter(User.username == request.username).first():
    raise HTTPException(status_code=400, detail='Username is taken')
  
  hashed_pass = auth_handler.get_password_hash(request.password)
  _user = User(username=request.username, password=hashed_pass)
  
  db.add(_user)
  db.commit()
  db.refresh(_user)
  return _user

# Login User
def login_user(db:Session, request: AuthSchema):
  user = db.query(User).filter(User.username == request.username).first()
  
  if user is None or not auth_handler.verify_password(request.password, user.password):
    raise HTTPException(status_code=401, detail='Invalid username and/or password')
    
  token = auth_handler.encode_token(user.username)
  return {"token": token}
  

# Get All Books
def get_book(db:Session, skip:int=0, limit:int=100):
  return db.query(Book).offset(skip).limit(limit).all()

# Get Book by ID
def get_book_by_id(db:Session, book_id:int):
  return db.query(Book).filter(Book.id == book_id).first()

# Create Book
def create_book(db:Session, request: RequestBook):
  _book = Book(title=request.parameter.title, description=request.parameter.description)
  db.add(_book)
  db.commit()
  db.refresh(_book)
  return _book

# Remove Book
def remove_book(db:Session, book_id:int):
  _book = get_book_by_id(db=db,book_id=book_id)
  db.delete(_book)
  db.commit()
  
# Update Book
def update_book(db:Session, book_id:int, title:str, description:str):
  _book = get_book_by_id(db=db, book_id=book_id)
  _book.title = title
  _book.description = description
  db.commit()
  db.refresh(_book)
  return _book