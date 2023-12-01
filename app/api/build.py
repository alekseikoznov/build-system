from typing import List, Union

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.schemas.build import Build
from app.services.get_tasks import get_tasks_for_build

router = APIRouter()


@router.post("/get_tasks", tags=["Get tasks"])
async def get_tasks(build_name: Build) -> Union[List[str], JSONResponse]:
    tasks = get_tasks_for_build(build_name)
    return tasks
