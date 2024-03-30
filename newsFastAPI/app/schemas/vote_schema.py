from pydantic import BaseModel
from .base_schema import ModelBaseInfo

class BaseVote(BaseModel):
  user_id: int
  post_id: int
  is_voted: bool
  
class VoteRequest(BaseVote):
  pass

class VoteIsReq(BaseModel):
  is_voted: bool