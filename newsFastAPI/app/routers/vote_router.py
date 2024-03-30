from fastapi import APIRouter, Depends, Body
from typing import Optional
from sqlalchemy.orm import Session
from ..core.config import get_db
from ..core.security import AuthHandler
from ..schemas.vote_schema import VoteRequest

auth_handler = AuthHandler()

router = APIRouter(
  prefix="/votes",
  tags=["votes"]
)

router.get("/")
def read_votes(user_id: Optional[int]=None, post_id:Optional[int]=None, credentials = Depends(auth_handler.auth_wrapper) , db:Session = Depends(get_db)):
  return {}

router.post("/")
def create_vote(req: VoteRequest, credentials = Depends(auth_handler.auth_wrapper), db:Session = Depends(get_db)):
  return {}

router.patch("/{id}")
def update_liked(id: int, is_voted:bool = Body(...), credentials = Depends(auth_handler.auth_wrapper), db:Session = Depends(get_db)):
  return {}