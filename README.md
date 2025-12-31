# Todo In-Memory Console Application

A simple, lightweight todo list application for tracking personal tasks. Data is stored in memory only and will be lost when the application closes.

## Features

- Add todos with title and optional description
- View all todos in a formatted list
- Update existing todos (title and description)
- Delete todos
- Console-based interaction
- No database or file storage required

## Requirements

- Python 3.13 or higher
- UV package manager

## Installation

1. Ensure you have Python 3.13+ installed:
   ```bash
   python --version
   ```

2. Ensure you have UV installed:
   ```bash
   uv --version
   ```

3. Install the application:
   ```bash
   uv pip install -e .
   ```

## Running the Application

After installation, run the application using UV:

```bash
uv run python -m src.todo
```

Or use the entry point directly:

```bash
uv run python src/todo/main.py
```

## Usage

The application presents a simple console menu:

```
============================================
           TODO APPLICATION
============================================

1. Add Todo
2. View All Todos
3. Update Todo
4. Delete Todo
5. Exit

Enter your choice (1-5):
```

### Adding a Todo

1. Select option `1` (Add Todo)
2. Enter the todo title (required)
3. Enter a description (optional, press Enter to skip)

### Viewing Todos

1. Select option `2` (View All Todos)
2. All todos will be displayed with ID, title, description, and creation timestamp

### Updating a Todo

1. Select option `3` (Update Todo)
2. Enter the ID of the todo to update
3. Enter a new title (leave blank to keep current)
4. Enter a new description (leave blank to keep current)

### Deleting a Todo

1. Select option `4` (Delete Todo)
2. Enter the ID of the todo to delete
3. Confirm with `y` to delete or `n` to cancel

### Exiting

Select option `5` (Exit) to close the application. Note: All data will be lost as it is stored in memory only.

## Project Structure

```
hackathon2/
├── pyproject.toml
├── README.md
└── src/
    └── todo/
        ├── __init__.py
        ├── main.py           # Entry point
        ├── manager.py        # Business logic and UI
        ├── models/
        │   ├── __init__.py
        │   └── todo.py      # Todo dataclass
        └── data/
            ├── __init__.py
            └── todo_store.py # In-memory storage
```

## License

This project is part of Panaversity Hackathon II.
