from fastapi import HTTPException, status
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..models import models
from ..schemas.vote_schema import VoteRequest
from ..core.security import AuthHandler

auth_handler = AuthHandler()

def get_votes(db:Session, user_id: Optional[int]=None, post_id:Optional[int]=None):
  query = db.query(models.VoteModel)
  if user_id:
    query.filter(models.VoteModel.user_id == user_id)
    
  if post_id:
    query.filter(models.VoteModel.post_id == post_id)
    
  return query.all()

def create_vote(db:Session, req:VoteRequest):
  vote_filter = db.query(models.VoteModel).filter(models.VoteModel.user_id == req.user_id, models.VoteModel.post_id == req.post_id).first()
  
  if vote_filter: 
    vote_update = update_is_voted(db, id=vote_filter.id, is_voted=not vote_filter.is_voted)  
    response = {"id": vote_update.id, "is_voted": vote_update.is_voted}
    return response
  else:
    new_vote = models.VoteModel(**req.dict())
    db.add(new_vote)
    db.commit()
    db.refresh(new_vote)
    return new_vote

def update_is_voted(db:Session, id:int, is_voted:bool):
  vote = db.query(models.VoteModel).filter(models.VoteModel.id == id).first()
  
  if not vote:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Vote ID {id} not found")
  
  vote.is_voted = is_voted
  db.commit()
  return vote