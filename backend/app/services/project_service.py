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

def update_project(
    project_id: int,
    user_id: int,
    project_data,
    db
):
    project = db.query(Project).filter(
        Project.id == project_id,
        Project.user_id == user_id
    ).first()

    if not project:
        return None

    project.name = project_data.name
    project.description = project_data.description

    db.commit()
    db.refresh(project)

    return project

def delete_project(
    project_id: int,
    user_id: int,
    db
):
    project = db.query(Project).filter(
        Project.id == project_id,
        Project.user_id == user_id
    ).first()

    if not project:
        return False

    db.delete(project)
    db.commit()

    return True