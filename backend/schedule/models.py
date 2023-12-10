# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import Mapped, mapped_column

# from libs.db import Base

# class Schedule(Base):
#     __tablename__ = "schedules"


#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
#     schedule_desc_input: Mapped[str] = mapped_column()
#     title: Mapped[str] = mapped_column()
#     description: Mapped[str] = mapped_column()
#     expected_start_at: Mapped[int] = mapped_column()
#     expected_duration: Mapped[int] = mapped_column()