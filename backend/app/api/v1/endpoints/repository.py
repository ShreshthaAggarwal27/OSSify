from pydantic import BaseModel
from fastapi import APIRouter, BackgroundTasks

from backend.app.services.repo_service import process_repository

router = APIRouter()


class RepoRequest(BaseModel):
    repo_url: str


@router.post("/analyze-repo")
def analyze_repo(request: RepoRequest, background_tasks: BackgroundTasks):
    repo_url = request.repo_url

    # Trigger background processing
    background_tasks.add_task(process_repository, repo_url)

    return {
        "status": "processing",
        "repo_url": repo_url,
        "message": "Repository analysis started in background"
    }