from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional, Union, TypeVar, Generic
from pydantic.generics import GenericModel

T = TypeVar("T")

class ModelBaseInfo(BaseModel):
    id: Optional[int]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    
class FindBase(BaseModel):
  ordering: Optional[str]
  page: Optional[int]
  page_size: Optional[Union[int, str]]

class SearchOptions(FindBase):
  total_count: Optional[int]

class FindResult(BaseModel):
  founds: Optional[List]
  search_options: Optional[SearchOptions]

class FindDateRange(BaseModel):
  created_at__lt: str
  created_at__lte: str
  created_at__gt: str
  created_at__gte: str

class Blank(BaseModel):
  pass

class Response (GenericModel, Generic[T]):
  code: str
  status: str
  message: str
  result: Optional[T]