# from pydantic import BaseModel

# class ScheduleInitializeRequest(BaseModel):
#     text: str


# class ScheduleCreateRequest(BaseModel):
#     title: str
#     description: str
#     expected_start_at: int
#     expected_duration: int

# class Schedule(BaseModel):
#     id: int
#     owner_id: int
#     schedule_desc_input: str
#     title: str
#     description: str
#     expected_start_at: int
#     expected_duration: int

#     class Config:
#         from_attributes = True

# class ScheduleCreateResponse(BaseModel):
#     schedule: Schedule