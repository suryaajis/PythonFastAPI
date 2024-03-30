from typing import Optional, List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..core.config import get_db
from ..services import post_service
from ..schemas.post_schema import PostRequest, PostSchema
from ..schemas.base_schema import Response
from ..models.models import PostModel
from ..core.security import AuthHandler

auth_handler = AuthHandler()

router = APIRouter(
  prefix="/posts",
  tags=["posts"]
)

# Alternate response
# def create_response(code: int, message: str, result=None):
#   return {
#     "code": str(code),
#     "status": "Ok" if code < 400 else "Error",
#     "message": message,
#     "result": result
#   }


@router.post('/')
async def create_post(request:PostRequest, credentials:int = Depends(auth_handler.auth_wrapper), db:Session=Depends(get_db)):
  post_service.create_post(db, request, credentials)
  return Response(code=str(status.HTTP_201_CREATED), status="Ok", message="Success created post", result=None).dict(exclude_none=True)

@router.get('/', response_model=List[PostSchema])
async def get_posts(user_id: Optional[int] = None, search: Optional[str]=None, credentials = Depends(auth_handler.auth_wrapper), db:Session=Depends(get_db)):
  posts = post_service.get_posts(db, 0, 100, user_id, search)
  return posts # Still not understand how to make output use Response Schema

@router.get('/{id}')
async def get_post_by_id(id:int, credentials = Depends(auth_handler.auth_wrapper), db:Session=Depends(get_db)):
  post = post_service.get_posts_by_id(db, id)
  return Response(code=str(status.HTTP_200_OK), status="Ok", message="Success read post", result=post).dict(exclude_none=True)

@router.put('/{id}')
async def update_post(id:int, request: PostRequest, credentials = Depends(auth_handler.auth_wrapper), db:Session=Depends(get_db)):
  post = post_service.update_post(db, id, request)
  return Response(code=str(status.HTTP_200_OK), status="Ok", message="Success updated book", result=post).dict(exclude_none=True)

@router.delete('/{id}')
async def delete_post(id: int, credentials = Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    post_service.delete_post(db, id)
    return Response(code=str(status.HTTP_200_OK), status="Ok", message="Success deleted book", result=None).dict(exclude_none=True)
