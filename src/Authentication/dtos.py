from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    username: str
    email: str
    password: str
    role: str = "EMPLOYEE"
    is_active: bool = True
    employee_id: Optional[int] = None

class LoginSchema(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserResponseSchema(BaseModel):
    id: int
    username: str
    email: str
    role: str
    is_active: bool
    employee_id: Optional[int] = None

    class Config:
        from_attributes = True


