from fastapi import HTTPException, status
from typing import Optional
from sqlalchemy.orm import Session
from ..schemas.vote_schema import VoteLikedReq, VoteRequest
from ..models.models import VoteModel
from ..core.security import AuthHandler

auth_handler = AuthHandler()

def get_votes(db:Session, user_id: Optional[int]=None, post_id:Optional[int]=None):
  query = db.query(VoteModel)
  
  if user_id:
    query.filter(VoteModel.user_id == user_id)
    
  if post_id:
    query.filter(VoteModel.post_id == post_id)
    
  return query.all()

def create_vote(db:Session, req:VoteRequest):
  vote_filter = db.query(VoteModel).filter(VoteModel.user_id == req.user_id, VoteModel.post_id == req.post_id).first()
  
  if vote_filter: 
    vote_update = update_is_voted(db, id=vote_filter.id, is_voted=not req.is_voted)
    return vote_update
  else:
    new_vote = VoteModel(**req.dict())
    db.add(new_vote)
    db.commit()
    db.refresh(new_vote)
    return new_vote

def update_is_voted(db:Session, id:int, is_voted:bool):
  vote = db.query(VoteModel).filter(VoteModel.id == id).first()
  
  if not vote:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Vote ID {id} not found")
  
  vote.is_voted = is_voted
  db.commit()
  return vote