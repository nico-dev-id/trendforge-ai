from app.models.project import Project


def create_project(
    db,
    current_user,
    project_data
):
    project = Project(
        name=project_data.name,
        description=project_data.description,
        user_id=current_user.id
    )

    db.add(project)
    db.commit()
    db.refresh(project)

    return project

def get_projects_by_user(user_id: int, db):
    return db.query(Project).filter(
        Project.user_id == user_id
    ).all()

def get_project_by_id(
    project_id: int,
    user_id: int,
    db
):
    return db.query(Project).filter(
        Project.id == project_id,
        Project.user_id == user_id
    ).first()