from typing import Annotated
from fastapi import APIRouter, Depends
from starlette.responses import RedirectResponse
from sqlalchemy.orm import Session
from sqlalchemy import select
from auth.models import User
from libs.auth import get_current_user
from utils.chain import optimize_data
from project.schemas import (
    ProjectCreateRequest,
    ProjectCreateResponse,
    ProjectInitializeRequest,
)
from project.models import Project
from libs.db import get_db

router = APIRouter(prefix="/project")

@router.post("/initialize")
def intialize(params: ProjectInitializeRequest, db_session: Annotated[Session, Depends(get_db)]):
    return {
        "id": None,
        "project": None
    }

@router.post("/", response_model=ProjectCreateResponse)
def create(params: ProjectCreateRequest, db_session: Annotated[Session, Depends(get_db)], current_user: Annotated[User, Depends(get_current_user)]):
    project = Project(
        owner_id = current_user.id,
        project_desc_input = "",
        title = params.title,
        description = optimize_data(params.description),
        timestamp = params.timestamp,
        expected_start_at = params.expected_start_at,
        expected_duration = params.expected_duration,
    )
   
    db_session.add(project)
    db_session.commit()

    # return {
    #     "project": project,
    # }
    return RedirectResponse(url='https://hooks.zapier.com/hooks/catch/17228727/3fc597i/', status_code=301)


@router.get("/")
def getAllProjects(db_session: Annotated[Session, Depends(get_db)], current_user: Annotated[User, Depends(get_current_user)]):
    db_projects = db_session.scalars(select(Project)).all()

    return db_projects

@router.get("/{id}")
def getOneProject(id: int, db_session: Annotated[Session, Depends(get_db)]):
    db_project = db_session.scalars(select(Project).where(Project.id == id)).first()

    return db_project

@router.put("/{id}")
def updateOneProject(id: int, params: ProjectCreateRequest, db_session: Annotated[Session, Depends(get_db)], current_user: Annotated[User, Depends(get_current_user)]):
    db_project = db_session.scalars(select(Project).where(Project.id == id)).first()
    db_session.delete(db_project)
    project = Project(
        owner_id = current_user.id,
        project_desc_input = "",
        title = params.title,
        description = params.description,
        expected_start_at = params.expected_start_at,
        expected_duration = params.expected_duration,
    )
    db_session.add(project)
    db_session.commit()

    return {
        "project" : project,
    }

@router.delete("/{id}")
def deleteOneProject(id: int, db_session: Annotated[Session, Depends(get_db)]):
    db_project = db_session.scalars(select(Project).where(Project.id == id)).first()
    db_session.delete(db_project)
    db_session.commit()
    
    return
