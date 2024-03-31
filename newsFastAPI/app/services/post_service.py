from typing import Optional
from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..schemas.post_schema import PostRequest
from ..models.models import PostModel, VoteModel

def get_posts(db:Session, skip:int=0, limit:int=100, user_id:Optional[int] = None, search:Optional[str]=None):
  try:
    query = db.query(PostModel)

    if user_id:
      query = query.filter(PostModel.user_id == user_id)

    if search:
      query = query.filter(PostModel.title.contains(search))

    result = query.limit(limit).offset(skip).all()
    return result
    # posts = db.query(PostModel, func.count(VoteModel.post_id).label("votes")).join(
    #   VoteModel, VoteModel.post_id == PostModel.id, isouter=True).group_by(PostModel.id).limit(limit).offset(skip).all()
    
    # # Process posts to create a JSON-compatible data structure
    # posts_data = []
    # for post, vote_count in posts:
    #   post_data = {
    #     "post": post,
    #     "votes": vote_count
    #   }
    #   posts_data.append(post_data)

    # # Serialize the data and return as a JSON response
    # json_data = jsonable_encoder(posts_data)
    # return JSONResponse(content=json_data)
  except Exception as e:
    raise ValueError("Error occurred while fetching and serializing posts") from e


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