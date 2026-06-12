from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.project import (
    ProjectCreate,
    ProjectResponse
)
from app.services.project_service import create_project
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