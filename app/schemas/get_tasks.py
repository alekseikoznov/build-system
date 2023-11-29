import yaml
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
builds_file_path = os.path.join(parent_dir, "builds", "builds.yaml")
tasks_file_path = os.path.join(parent_dir, "builds", "tasks.yaml")

with open(tasks_file_path, "r") as tasks_file:
    tasks_data = yaml.safe_load(tasks_file)

with open(builds_file_path, "r") as builds_file:
    builds_data = yaml.safe_load(builds_file)
