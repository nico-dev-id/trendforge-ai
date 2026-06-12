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