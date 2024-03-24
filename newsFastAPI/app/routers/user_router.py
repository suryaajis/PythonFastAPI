from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..core.config import get_db
from ..schemas.user_schema import UserRequest, UserDisableRequest, UserLoginRequest
from ..schemas.base_schema import Response
from ..services import user_service

router = APIRouter(
  prefix="/users",
  tags=["users"]
)

# Auth User Routers
@router.post("/register")
def register_user(request:UserRequest, db:Session=Depends(get_db)):
  data = user_service.register_user(db, request)
  return Response(code="201", status="Ok", message="Success register user", result=data).dict(exclude_none=True)

@router.post("/login")
def login_user(request: UserLoginRequest, db:Session=Depends(get_db)):
  data = user_service.login_user(db, request)
  return Response(code="200", status="Ok", message="Success login user", result=data).dict(exclude_none=True)



# User Routers
@router.get("/")
def read_user(db:Session=Depends(get_db)):
  data = user_service.get_users(db)
  return Response(code=str(status.HTTP_200_OK), status="Ok", message="Success read all users", result=data).dict(exclude_none=True)

@router.get("/{id}")
def read_user_by_id(id:int, db:Session=Depends(get_db)):
  data = user_service.get_user_by_id(db, id)
  return Response(code=str(status.HTTP_200_OK), status="Ok", message="Success read user", result=data).dict(exclude_none=True)

@router.patch("/{id}")
def disable_user(id: int, request: UserDisableRequest, db:Session=Depends(get_db)):
  data = user_service.disable_user(db, id, is_active=request.is_active)
  response = {"email": data.email, "is_active": data.is_active}
  return Response(code=str(status.HTTP_200_OK), status="Ok", message="Success change activation user", result=response).dict(exclude_none=True)
