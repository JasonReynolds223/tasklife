from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from libs.db import Base

class Project(Base):
    __tablename__ = "projects"


    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    project_desc_input: Mapped[str] = mapped_column()
    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    timestamp: Mapped[int] = mapped_column()
    expected_start_at: Mapped[int] = mapped_column()
    expected_duration: Mapped[int] = mapped_column()