from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..core.config import get_db
from ..schemas.user_schema import UserRequest
from ..schemas.base_schema import Response
from ..services import user_service

router = APIRouter(
  prefix="/users",
  tags=["users"]
)


@router.post("/")
def register_user(request:UserRequest, db:Session=Depends(get_db())):
  return {}

@router.get("/")
def read_user(db:Session=Depends(get_db())):
  users = user_service.get_users(db)
  return Response(code=str(status.HTTP_200_OK), status="Ok", message="Success read all users", result=users).dict(exclude_none=True)

@router.get("/{id}")
def read_user_by_id(id:int, db:Session=Depends(get_db())):
  user = user_service.get_user_by_id(db, id)
  return Response(code=str(status.HTTP_200_OK), status="Ok", message="Success read user", result=user).dict(exclude_none=True)

@router.patch("/{id}")
def disable_user(id: int, is_active:bool, db:Session=Depends(get_db())):
  updated_user = user_service.disable_user(db, id, is_active)
  return Response(code=str(status.HTTP_200_OK), status="Ok", message="Success change activation user", result=updated_user).dict(exclude_none=True)
