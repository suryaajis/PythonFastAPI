from fastapi import APIRouter, Depends, Body
from typing import Optional, List
from sqlalchemy.orm import Session
from ..core.config import get_db
from ..core.security import AuthHandler
from ..schemas.vote_schema import VoteRequest, VoteSchema
from ..services import vote_service

auth_handler = AuthHandler()

router = APIRouter(
  prefix="/votes",
  tags=["votes"]
)

@router.get("/", response_model=List[VoteSchema])
def read_votes(user_id: Optional[int]=None, post_id:Optional[int]=None, credentials = Depends(auth_handler.auth_wrapper) , db:Session = Depends(get_db)):
  response = vote_service.get_votes(db, user_id, post_id)
  return response

@router.post("/")
def create_vote(req: VoteRequest, credentials = Depends(auth_handler.auth_wrapper), db:Session = Depends(get_db)):
  response = vote_service.create_vote(db, req)
  return response

@router.patch("/{id}")
def update_liked(id: int, is_voted:bool = Body(...), credentials = Depends(auth_handler.auth_wrapper), db:Session = Depends(get_db)):
  response = vote_service.update_is_voted(db, id, is_voted)
  return response