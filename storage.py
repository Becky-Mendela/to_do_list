
import json


def read_tasks(file_path):
    try:
        with open(file_path, 'r') as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []

    return tasks


def write_tasks(file_path, tasks):
    try:
        with open(file_path, 'w') as f:
            json.dump(tasks, f, indent=2)
    except IOError as e:
        print(f"Error saving tasks: {e}")