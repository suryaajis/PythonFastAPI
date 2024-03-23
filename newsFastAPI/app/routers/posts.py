from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..core.config import get_db
from ..services import post_service
from ..schemas.post_schema import PostSchema, PostRequest
from ..schemas.base_schema import Response

router = APIRouter(
  prefix="/posts",
  tags=["posts"]
)

@router.post('/')
async def create_post(request:PostRequest, db:Session=Depends(get_db)):
  post_service.create_post(db, request)
  return Response(code=str(status.HTTP_201_CREATED), status="Ok", message="Success created post", result=None).dict(exclude_none=True)

@router.get('/')
async def get_posts(db:Session=Depends(get_db)):
  posts = post_service.get_posts(db, 0, 100)
  return Response(code=str(status.HTTP_200_OK), status="Ok", message="Success read all posts", result=posts).dict(exclude_none=True)

@router.get('/{id}')
async def get_post_by_id(id:int, db:Session=Depends(get_db)):
  post = post_service.get_posts_by_id(db, id)
  return Response(code=str(status.HTTP_200_OK), status="Ok", message="Success read post", result=post).dict(exclude_none=True)

@router.put('/{id}')
async def update_post(id:int, request: PostRequest, db:Session=Depends(get_db)):
  post = post_service.update_post(db, id, request)
  return Response(code=str(status.HTTP_200_OK), status="Ok", message="Success updated book", result=post).dict(exclude_none=True)

@router.delete('/{id}')
async def delete_post(id: int, db: Session = Depends(get_db)):
    post_service.delete_post(db, id)
    return Response(code=str(status.HTTP_200_OK), status="Ok", message="Success deleted book", result=None).dict(exclude_none=True)
