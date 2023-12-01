import yaml
from fastapi.testclient import TestClient

from app.main import app
from app.services.get_tasks import builds_file_path

with open(builds_file_path, "r") as builds_file:
    builds_data = yaml.safe_load(builds_file)


builds = builds_data["builds"]
real_build_name = builds[0]["name"]
client = TestClient(app)


def test_get_tasks() -> None:
    response = client.post("/get_tasks", json={"build": real_build_name})
    assert response.status_code == 200
    assert response.json()


def test_get_tasks_not_found() -> None:
    response = client.post("/get_tasks", json={"build": "nonexistent_build"})
    assert response.status_code == 404
    assert "Build nonexistent_build not found." in response.json()["detail"]


def test_sorted_tasks() -> None:
    response = client.post("/get_tasks", json={"build": real_build_name})
    assert response.status_code == 200

    sorted_tasks = response.json()
    for task in sorted_tasks:
        assert isinstance(task, str)
