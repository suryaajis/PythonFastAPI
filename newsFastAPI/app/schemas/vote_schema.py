from pydantic import BaseModel
from .base_schema import ModelBaseInfo
from .user_schema import UserResponse
from .post_schema import PostResponse

class BaseVote(BaseModel):
  user_id: int
  post_id: int
  is_voted: bool
  
class VoteRequest(BaseModel):
  user_id:int
  post_id: int
  
class VoteSchema(BaseVote):
  ...
  user: UserResponse
  post: PostResponse
  
