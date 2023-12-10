from pydantic import BaseModel

from auth.models import UserRole


class User(BaseModel):
    username: str
    email: str | None = None

    class Config:
        from_attributes = True


class LoginRequest(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    user: User


class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str
    role: UserRole


class ReadAuthMeResponse(BaseModel):
    user: User
