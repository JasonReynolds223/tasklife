# from typing import Annotated
# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from sqlalchemy import select
# from auth.models import User
# from libs.auth import get_current_user

# from schedule.schemas import (
#     ScheduleCreateRequest,
#     ScheduleCreateResponse,
#     ScheduleInitializeRequest,
# )
# from schedule.models import Schedule
# from libs.db import get_db

# router = APIRouter(prefix="/schedule")

# @router.post("/initialize")
# def intialize(params: ScheduleInitializeRequest, db_session: Annotated[Session, Depends(get_db)]):
#     return {
#         "id": None,
#         "project": None
#     }

# @router.post("/", response_model=ScheduleCreateResponse)
# def create(params: ScheduleCreateRequest, db_session: Annotated[Session, Depends(get_db)], current_user: Annotated[User, Depends(get_current_user)]):
    
#     schedule = Schedule(
#         owner_id = current_user.id,
#         schedule_desc_input = "",
#         title = params.title,
#         description = params.description,
#         expected_start_at = params.expected_start_at,
#         expected_duration = params.expected_duration,
#     )
#     db_session.add(schedule)
#     db_session.commit()

#     return {
#         "schedule": schedule,
#     }

# @router.get("/{id}")
# def getOneSchedule(id: int, db_session: Annotated[Session, Depends(get_db)]):
#     db_schedule= db_session.scalars(select(Schedule).where(Schedule.id == id)).first()

#     return db_schedule

# @router.put("/{id}")
# def updateOneSchedule(id: int, params: ScheduleCreateRequest, db_session: Annotated[Session, Depends(get_db)], current_user: Annotated[User, Depends(get_current_user)]):
#     db_schedule = db_session.scalars(select(Schedule).where(Schedule.id == id)).first()
#     db_session.delete(db_schedule)
#     schedule = Schedule(
#         owner_id = current_user.id,
#         schedule_desc_input = "",
#         title = params.title,
#         description = params.description,
#         expected_start_at = params.expected_start_at,
#         expected_duration = params.expected_duration,
#     )
#     db_session.add(schedule)
#     db_session.commit()

#     return {
#         "project" : schedule,
#     }

# @router.delete("/{id}")
# def deleteOneSchedule(id: int, db_session: Annotated[Session, Depends(get_db)]):
#     db_schedule = db_session.scalars(select(Schedule).where(Schedule.id == id)).first()
#     db_session.delete(db_schedule)
#     db_session.commit()
    
#     return
