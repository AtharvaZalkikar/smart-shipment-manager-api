from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database.db import get_session
from app.schemas.shipment import UserCreate, UserResponse, LoginRequest, TokenResponse
from app.services import auth_service

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, session: Session = Depends(get_session)):

    db_user = auth_service.create_user(
        session,
        user.model_dump()
    )

    if not db_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    return db_user




@router.post("/login", response_model=TokenResponse)
def login(user: LoginRequest, session: Session = Depends(get_session)):

    token = auth_service.authenticate_user(
        session,
        user.email,
        user.password
    )

    if not token:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return {
        "access_token": token,
        "token_type": "bearer"
    }