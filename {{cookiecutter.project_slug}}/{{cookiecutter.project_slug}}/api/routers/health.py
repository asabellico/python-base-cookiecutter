from fastapi import APIRouter
from fastapi import status
from pydantic import BaseModel


router: APIRouter = APIRouter(prefix="/health", tags=["health"])

class HealthResponse(BaseModel):
    status: str

@router.get("/", response_model=HealthResponse, status_code=status.HTTP_200_OK)
async def healthcheck():
    return HealthResponse(
        status="ok"
    )
