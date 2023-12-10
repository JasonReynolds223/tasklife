from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from libs.db import Base



class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] =  mapped_column(primary_key=True, autoincrement=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"))
    parent_task_id: Mapped[int] = mapped_column(ForeignKey("tasks.id"))
    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    expected_start_at: Mapped[int] = mapped_column()
    expected_duration: Mapped[int] = mapped_column()
