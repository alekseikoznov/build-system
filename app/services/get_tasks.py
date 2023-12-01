import yaml
import os
from fastapi.responses import JSONResponse

from app.schemas.build import Build

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
builds_file_path = os.path.join(parent_dir, "builds", "builds.yaml")
tasks_file_path = os.path.join(parent_dir, "builds", "tasks.yaml")

with open(tasks_file_path, "r") as tasks_file:
    tasks_data = yaml.safe_load(tasks_file)

with open(builds_file_path, "r") as builds_file:
    builds_data = yaml.safe_load(builds_file)


def tasks_sort(build_tasks, all_tasks):
    tasks = {}
    for task_data in all_tasks:
        task_name = task_data.get("name")
        tasks[task_name] = {"dependencies": task_data.get("dependencies", [])}

    sorted_tasks = []
    visited = set()

    def visit(task_name):
        if task_name in visited:
            return
        visited.add(task_name)
        dependencies = tasks[task_name].get("dependencies", [])
        for dependency in dependencies:
            visit(dependency)
        sorted_tasks.append(task_name)

    for task_name in build_tasks:
        visit(task_name)

    return sorted_tasks


def get_tasks_for_build(build_name: Build):
    build_name = build_name.dict().get('build')

    selected_build = next((b for b in builds_data["builds"] if b.get("name") == build_name), None)

    if selected_build is None:
        return JSONResponse(status_code=404, content={"detail": f"Build {build_name} not found."})

    build_tasks = selected_build.get("tasks", [])
    sorted_tasks = tasks_sort(build_tasks, tasks_data.get("tasks", []))
    return sorted_tasks
