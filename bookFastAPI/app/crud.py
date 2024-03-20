from sqlalchemy.orm import Session
from model import Book
from schemas import BookSchema, RequestBook

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