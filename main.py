"""
Simple CLI-based task tracker application.
"""

import os
import json

FILE_PATH = "tasks.json"

def startup_check():
    # Try to load existing tasks
    try:
        with open(FILE_PATH, "r") as f:
            tasks = json.load(f)
    
    # If file doesn't exist or is invalid, create empty list
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []

        # Save empty list to file
        with open(FILE_PATH, "w") as f:
            json.dump(tasks, f, indent=2)
    
    return tasks

task_list = []  # main task list

def main():
    tasks = startup_check()

def add_task(task_list):
    pass

def update_task(task_list):
    pass

def delete_task(task_list):
    pass
