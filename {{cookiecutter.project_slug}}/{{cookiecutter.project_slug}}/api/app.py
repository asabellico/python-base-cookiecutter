# app.py
import uvicorn
from fastapi import FastAPI

from .routers import health

app = FastAPI(
    title="{{cookiecutter.project_slug}} API",
    description="...",
    version="{{cookiecutter.version}}",
    docs_url="/",
)

app.include_router(health.router)


if __name__ == "__main__":
    uvicorn.run(app)
