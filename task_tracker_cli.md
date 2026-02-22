# Project 1: Task Tracker

## Requirements

Application should run from command line, accept user actions and inputs as arguments, and store tasks in a JSON file.

- Add, Update, and Delete tasks
- Mark a task as in progress or done
- List all tasks
- List all tasks that are done
- List all tasks that are not done
- List all tasks that are in progress

### Tips

- JSON file should be created if it does not exist
- Do NOT use external libraries
- Handle errors and edge cases gracefully

### Task Properties

Consider making a `task` class

- `id`: A unique identifier for the task
- `description`: A short description of the class
- `status`: The status of the task (`todo`, `in-progress`, `done`)
- `createdAt`: The date and time when the task was created
- `updatedAt`: The date and time when the task was last updated

Make sure to add these properties to the JSON file when adding a new task and update them when updating a task

### Build order

1. JSON load/saves
2. Task classes
3. Add task
4. List tasks
5. Delete
6. Update
7. Status changes
8. Filters
9. Edge cases
