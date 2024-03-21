from fastapi import APIRouter, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import AuthSchema, RequestBook, Response
import controller

router = APIRouter()

def get_db():
  db = SessionLocal()
  try: 
    yield db
  finally:
    db.close()
    
@router.post('/register')
async def register(auth_details: AuthSchema, db:Session=Depends(get_db)):
  _user = controller.register_user(db, auth_details)
  return Response(code="201", status="Ok", message="Success register user", result=_user).dict(exclude_none=True)
  
@router.post('/login')
async def login(auth_details: AuthSchema, db:Session=Depends(get_db)):
  token_user = controller.login_user(db, auth_details)
  return Response(code="200", status="Ok", message="Success login user", result=token_user).dict(exclude_none=True)
    
@router.post('/create-book')
async def create_book(request:RequestBook, db:Session=Depends(get_db)):
  controller.create_book(db, request)
  return Response(code="201", status="Ok", message="Success created book", result=None).dict(exclude_none=True)

@router.get('/get-books')
async def get_books(db:Session=Depends(get_db)):
  _book = controller.get_book(db, 0, 100)
  return Response(code="200", status="Ok", message="Success read all books", result=_book).dict(exclude_none=True)

@router.get('/get-book/{id}')
async def get_book_by_id(id:int, db:Session=Depends(get_db)):
  _book = controller.get_book_by_id(db, id)
  return Response(code="200", status="Ok", message="Success read book", result=_book).dict(exclude_none=True)

@router.put('/update-book/{id}')
async def update_book(id:int, request: RequestBook, db:Session=Depends(get_db)):
  _book = controller.update_book(db, id, request.parameter.title, request.parameter.description)
  return Response(code="200", status="Ok", message="Success updated book", result=_book).dict(exclude_none=True)

@router.delete('/delete-book/{id}')
async def delete_book(id: int, db: Session = Depends(get_db)):
    controller.remove_book(db, id)
    return Response(code="200", status="Ok", message="Success deleted book", result=None).dict(exclude_none=True)
