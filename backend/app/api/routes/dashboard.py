from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr

from app.api.deps import get_current_user

router = APIRouter(prefix="/auth", tags=["auth"])


class LoginRequest(BaseModel):
    username: str
    password: str


@router.post("/login")
def login(payload: LoginRequest):
    if payload.username == "admin" and payload.password == "StrongPass123!":
        return {
            "access_token": "demo-access-token",
            "refresh_token": "demo-refresh-token",
            "token_type": "bearer",
        }
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")


@router.post("/register")
def register():
    return {"message": "User registration endpoint scaffolded"}


@router.post("/refresh")
def refresh():
    return {"message": "JWT refresh endpoint scaffolded"}


@router.post("/logout")
def logout():
    return {"message": "Logout successful"}


@router.get("/me")
def me(current_user=Depends(get_current_user)):
    return {"user": current_user}
