from fastapi import FastAPI
from app.api import auth, user, project


def create_app():
    app = FastAPI(
        title="TrendForge AI",
        version="1.0.0"
    )

    app.include_router(auth.router)
    app.include_router(user.router)
    app.include_router(project.router)

    @app.get("/")
    def root():
        return {"message": "TrendForge AI Running"}

    return app


app = create_app()