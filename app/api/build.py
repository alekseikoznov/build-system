from typing import List

from app.schemas.build import Build
from app.services.get_tasks import get_tasks_for_build

from fastapi import APIRouter

router = APIRouter()


@router.post('/get_tasks', tags=['Get tasks'])
async def get_tasks(build_name: Build) -> List[str]:
    tasks = get_tasks_for_build(build_name)
    return tasks
