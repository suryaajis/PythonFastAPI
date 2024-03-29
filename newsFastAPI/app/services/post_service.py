from typing import Optional
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from ..schemas.post_schema import PostRequest
from ..models.models import PostModel

def get_posts(db:Session, skip:int=0, limit:int=100, user_id:Optional[int] = None):
  if user_id:
    return db.query(PostModel).filter(PostModel.user_id == user_id).offset(skip).limit(limit).all()
  
  return db.query(PostModel).offset(skip).limit(limit).all()

def get_posts_by_id(db:Session, post_id:int):
  post = db.query(PostModel).filter(PostModel.id == post_id).first()
  
  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post ID {post_id} not found")
  
  return post

def create_post(db:Session, req:PostRequest, credentials:int):
  new_post = PostModel(user_id=credentials, **req.dict())
  db.add(new_post)
  db.commit()
  db.refresh(new_post)
  return new_post

def update_post(db:Session, post_id:int, req:PostRequest):
  post_query = db.query(PostModel).filter(PostModel.id == post_id)
  post_selected = post_query.first()
  
  if not post_selected:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post ID {post_id} not found")
  
  post_query.update(req.dict())
  
  db.commit()
  return post_query.first()

def delete_post(db:Session, post_id:int):
  post = get_posts_by_id(db, post_id)
  db.delete(post)
  db.commit()
  return post