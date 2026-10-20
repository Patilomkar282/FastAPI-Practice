from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.Authentication.model import User
from src.Authentication.dtos import UserSchema, LoginSchema
from src.Employee.model import Employee
from pwdlib import PasswordHash
from src.utils.settings import settings
from datetime import datetime, timedelta, timezone
from jose import jwt

password_hash = PasswordHash.recommended()

def get_password_hash(password: str) -> str:
    return password_hash.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hash.verify(plain_password, hashed_password)

def create_user(body: UserSchema, db: Session):
 
    if db.query(User).filter(User.email == body.email).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
   
    if db.query(User).filter(User.username == body.username).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already taken")

  
    if body.employee_id is not None:
        employee = db.query(Employee).filter(Employee.id == body.employee_id).first()
        if not employee:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"Employee with id {body.employee_id} does not exist"
            )

    hashed_password = get_password_hash(body.password)
    new_user = User(
        username=body.username,
        email=body.email,
        hashed_password=hashed_password,
        role=body.role,
        is_active=body.is_active,
        employee_id=body.employee_id
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def login(body: LoginSchema, db: Session):
    user = db.query(User).filter(User.email == body.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
    
    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Account is deactivated")
    
    if not verify_password(body.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")

    exp_time = datetime.now(timezone.utc) + timedelta(minutes=settings.EXP_TIME)
    payload = {
        "sub": str(user.id),
        "email": user.email,
        "role": user.role,
        "exp": exp_time
    }
    
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}

    
    