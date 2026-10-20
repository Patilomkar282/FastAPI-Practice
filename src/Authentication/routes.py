from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.Authentication.dtos import UserSchema, UserResponseSchema, LoginSchema, TokenResponse
from src.Authentication.model import User
from src.Authentication.dependencies import get_current_user
import src.Authentication.controller as controller

userrouter = APIRouter(prefix="/users", tags=["Users"])

@userrouter.post("/create", status_code=status.HTTP_201_CREATED, response_model=UserResponseSchema)
def create_user(body: UserSchema, db: Session = Depends(get_db)):
    return controller.create_user(body, db)

@userrouter.post("/login", status_code=status.HTTP_200_OK, response_model=TokenResponse)
def login(body: LoginSchema, db: Session = Depends(get_db)):
    return controller.login(body, db)

@userrouter.get("/me", status_code=status.HTTP_200_OK, response_model=UserResponseSchema)
def get_current_user_profile(current_user: User = Depends(get_current_user)):
    return current_user



