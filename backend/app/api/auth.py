from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.auth_service import register_user, authenticate_user
from app.schemas.user import ( UserCreate, UserResponse, LoginResponse )

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post(
    "/register",
    response_model=UserResponse
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return register_user(db, user)


@router.post(
    "/login",
    response_model=LoginResponse
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    return authenticate_user(
        db,
        form_data.username,
        form_data.password
    )