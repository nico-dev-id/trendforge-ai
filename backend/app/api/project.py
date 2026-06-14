from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.project import (ProjectCreate, ProjectUpdate, ProjectResponse)
from app.services.project_service import (create_project, get_projects_by_user, get_project_by_id, update_project, delete_project)
from app.core.deps import get_current_user


router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


@router.post(
    "",
    response_model=ProjectResponse
)
def create_new_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return create_project(
        db,
        current_user,
        project
    )

@router.get(
    "",
    response_model=list[ProjectResponse]
)
def get_projects(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return get_projects_by_user(
        current_user.id,
        db
    )

@router.get(
    "/{project_id}",
    response_model=ProjectResponse
)
def get_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    project = get_project_by_id(
        project_id,
        current_user.id,
        db
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return project

@router.put(
    "/{project_id}",
    response_model=ProjectResponse
)
def update_project_endpoint(
    project_id: int,
    project: ProjectUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    updated_project = update_project(
        project_id,
        current_user.id,
        project,
        db
    )

    if not updated_project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return updated_project

@router.delete("/{project_id}")
def delete_project_endpoint(
    project_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    deleted = delete_project(
        project_id,
        current_user.id,
        db
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return {
        "message": "Project deleted successfully"
    }