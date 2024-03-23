from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from ..schemas.post_schema import Post

def get_posts(db:Session, skip:int=0, limit:int=100):
  return db.query(Post).offset(skip).limit(limit).all()

def get_posts_by_id(db:Session, post_id:int):
  post = db.query(Post).filter(Post.id == post_id).first()
  
  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post ID {post_id} not found")
  
  return post

def create_post(db:Session, req:Post):
  new_post = Post(title=req.title, content=req.content, published=req.published)
  db.add(new_post)
  db.commit()
  db.refresh(new_post)
  return new_post

def update_post(db:Session, post_id:int, req:Post):
  post_query = db.query(Post).filter(Post.id == post_id)
  post_selected = post_query.first()
  
  if not post_selected:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post ID {post_id} not found")
  
  post_query.update(req.dict(), synchronize_session=False)
  
  db.commit()
  db.refresh(post_query)
  return post_query.first()

def delete_post(db:Session, post_id:int):
  post = get_posts_by_id(db, post_id)
  db.delete(post)
  db.commit()
  return post