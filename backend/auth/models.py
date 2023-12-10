import enum
from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column

from libs.db import Base

class UserRole(enum.Enum):
    ADMIN = 'admin'
    PROJECT_MANAGER = 'project_manager'
    DEVELOPER = 'developer'

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str] = mapped_column()
    role: Mapped[UserRole] = mapped_column(Enum(UserRole, native_enum=False), default=UserRole.PROJECT_MANAGER)
