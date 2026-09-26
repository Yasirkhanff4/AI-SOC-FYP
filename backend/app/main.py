from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.core.security import create_access_token, hash_password, verify_password
from app.database import get_db
from app.models import User

router = APIRouter(prefix="/auth", tags=["auth"])


class LoginRequest(BaseModel):
    username: str
    password: str


class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str


@router.post("/login")
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    user = db.execute(select(User).where(User.username == payload.username)).scalar_one_or_none()
    if user is None or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token = create_access_token(user.username)
    return {
        "access_token": access_token,
        "refresh_token": "demo-refresh-token",
        "token_type": "bearer",
        "user": {"username": user.username, "role": user.role},
    }


@router.post("/register")
def register(payload: RegisterRequest, db: Session = Depends(get_db)):
    existing = db.execute(select(User).where(User.username == payload.username)).scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    user = User(
        username=payload.username,
        email=payload.email,
        password_hash=hash_password(payload.password),
        role="SOC_ANALYST",
        is_active=True,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "User created successfully", "username": user.username}


@router.post("/refresh")
def refresh():
    return {"message": "JWT refresh endpoint scaffolded"}


@router.post("/logout")
def logout():
    return {"message": "Logout successful"}


@router.get("/me")
def me(current_user=Depends(get_current_user)):
    return {"user": current_user}
