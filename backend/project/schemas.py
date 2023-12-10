from pydantic import BaseModel

class ProjectInitializeRequest(BaseModel):
    text: str


class ProjectCreateRequest(BaseModel):
    title: str
    description: str
    timestamp: int
    expected_start_at: int
    expected_duration: int

class Project(BaseModel):
    id: int
    owner_id: int
    project_desc_input: str
    title: str
    description: str
    expected_start_at: int
    expected_duration: int

    class Config:
        from_attributes = True

class ProjectCreateResponse(BaseModel):
    project: Project


