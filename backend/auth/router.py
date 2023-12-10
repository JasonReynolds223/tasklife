from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, insert
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from auth.schemas import (
    LoginRequest,
    LoginResponse,
    RegisterRequest,
    ReadAuthMeResponse,
)
from auth.models import User
from libs.db import get_db
from libs.auth import (
    verify_password,
    create_access_token,
    get_password_hash,
    get_current_user,
)

router = APIRouter(prefix="/auth")


@router.post("/login", response_model=LoginResponse)
def login(params: LoginRequest, db_session: Annotated[Session, Depends(get_db)]):
    db_user = db_session.scalars(select(User).where(User.email == params.email)).first()
    if not db_user or not verify_password(params.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(db_user.email)

    return {"access_token": access_token, "user": db_user}


@router.post("/register")
def register(params: RegisterRequest, db_session: Annotated[Session, Depends(get_db)]):
    username = db_session.scalars(
        insert(User).returning(User.username),
        [
            {
                "username": params.username,
                "email": params.email,
                "hashed_password": get_password_hash(params.password),
                "role": params.role,
            }
        ],
    ).first()
    db_session.commit()

    access_token = create_access_token(username)

    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=ReadAuthMeResponse)
async def read_auth_me(current_user: Annotated[User, Depends(get_current_user)]):
    return {"user": current_user}


@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db_session: Annotated[Session, Depends(get_db)],
):
    db_user = db_session.scalars(
        select(User).where(User.email == form_data.username)
    ).first()

    if not db_user or not verify_password(form_data.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(db_user.email)

    return {"access_token": access_token, "token_type": "bearer"}
