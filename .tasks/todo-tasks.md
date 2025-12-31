# Todo In-Memory Console Application - Implementation Tasks

## Setup Tasks

| ID | Task | Description | Dependencies |
|----|------|-------------|--------------|
| T-01 | Create pyproject.toml | Create UV-compatible pyproject.toml with Python 3.13+ requirement | None |
| T-02 | Create src directory structure | Create src/ with all subdirectories (__init__.py files) | T-01 |
| T-03 | Create data directory structure | Create data/ subdirectory under src/ with __init__.py | T-02 |

## Model Tasks

| ID | Task | Description | Dependencies |
|----|------|-------------|--------------|
| T-04 | Create Todo model class | Create src/models/todo.py with dataclass (id, title, description, created_at) | T-02 |
| T-05 | Export Todo from models | Create src/models/__init__.py to export Todo class | T-04 |

## Data Layer Tasks

| ID | Task | Description | Dependencies |
|----|------|-------------|--------------|
| T-06 | Create TodoStore class | Create src/data/todo_store.py with in-memory Dict storage and ID counter | T-04 |
| T-07 | Export TodoStore | Create src/data/__init__.py to export TodoStore class | T-06 |

## Service Layer Tasks

| ID | Task | Description | Dependencies |
|----|------|-------------|--------------|
| T-08 | Create TodoService class | Create src/services/todo_service.py with CRUD operations | T-04, T-07 |
| T-09 | Export TodoService | Create src/services/__init__.py to export TodoService class | T-08 |

## Utility Tasks

| ID | Task | Description | Dependencies |
|----|------|-------------|--------------|
| T-10 | Create validators module | Create src/utils/validators.py with input validation functions | None |
| T-11 | Export validators | Create src/utils/__init__.py to export validation functions | T-10 |

## UI Layer Tasks

| ID | Task | Description | Dependencies |
|----|------|-------------|--------------|
| T-12 | Create Menu class | Create src/ui/menu.py with console display and input collection | T-08, T-10 |
| T-13 | Export Menu | Create src/ui/__init__.py to export Menu class | T-12 |

## Entry Point Tasks

| ID | Task | Description | Dependencies |
|----|------|-------------|--------------|
| T-14 | Create main.py entry point | Create src/main.py with application initialization and main loop | T-12 |

## Finalization Tasks

| ID | Task | Description | Dependencies |
|----|------|-------------|--------------|
| T-15 | Create root __init__.py | Create src/__init__.py for package marker | All src tasks |
| T-16 | Verify project structure | Verify all files exist and imports are correct | All tasks |

## Implementation Order

```
T-01 ──> T-02 ──> T-03
 │        │
 │        └──> T-04 ──> T-05
 │                  │
 │                  └──> T-06 ──> T-07
 │                            │
 │                            └──> T-08 ──> T-09
 │
 └──> T-10 ──> T-11
              │
              └──> T-12 ──> T-13
                        │
                        └──> T-14
                              │
                              └──> T-15
                                    │
                                    └──> T-16
```

## Task Details

### T-01: Create pyproject.toml
- Create `pyproject.toml` in project root
- Set name to "todo-app"
- Set version to "0.1.0"
- Set requires-python to ">=3.13"
- Set dependencies to empty list (no external libraries)
- Configure build-system with hatchling

### T-02: Create src directory structure
- Create `src/` directory
- Create `src/models/`, `src/services/`, `src/ui/`, `src/utils/`, `src/data/` subdirectories
- Create empty `__init__.py` files in each directory

### T-03: Create data directory structure
- Create `src/data/` directory (already partially created in T-02)
- Ensure `__init__.py` exists in src/data/

### T-04: Create Todo model class
- Create `src/models/todo.py`
- Define `Todo` dataclass with:
  - `id: int` - unique identifier
  - `title: str` - required todo title
  - `description: str | None` - optional description
  - `created_at: datetime` - creation timestamp
- Include dataclass decorator and imports

### T-05: Export Todo from models
- Create `src/models/__init__.py`
- Export `Todo` class for import convenience

### T-06: Create TodoStore class
- Create `src/data/todo_store.py`
- Define `TodoStore` class with:
  - `_todos: dict[int, Todo]` - private storage dictionary
  - `_next_id: int` - private ID counter starting at 1
- Implement methods:
  - `add(todo: Todo) -> int` - returns new todo ID
  - `get_all() -> list[Todo]` - returns all todos sorted by ID
  - `get_by_id(id: int) -> Todo | None` - returns todo or None
  - `update(id: int, **kwargs) -> bool` - updates fields, returns success
  - `delete(id: int) -> bool` - removes todo, returns success

### T-07: Export TodoStore
- Create `src/data/__init__.py`
- Export `TodoStore` class

### T-08: Create TodoService class
- Create `src/services/todo_service.py`
- Define `TodoService` class with TodoStore dependency
- Implement methods:
  - `create_todo(title: str, description: str | None) -> int`
  - `get_all_todos() -> list[Todo]`
  - `update_todo(id: int, title: str | None, description: str | None) -> bool`
  - `delete_todo(id: int) -> bool`
- Add business logic validation (non-empty title, etc.)

### T-09: Export TodoService
- Create `src/services/__init__.py`
- Export `TodoService` class

### T-10: Create validators module
- Create `src/utils/validators.py`
- Implement validation functions:
  - `validate_non_empty(input: str, field_name: str) -> str` - raises ValueError if empty
  - `validate_yes_no(input: str) -> bool` - returns True for 'y', False for 'n', raises ValueError otherwise
  - `validate_todo_id(input: str, store: TodoStore) -> int` - parses and validates ID exists
- Document functions with docstrings

### T-11: Export validators
- Create `src/utils/__init__.py`
- Export validation functions

### T-12: Create Menu class
- Create `src/ui/menu.py`
- Define `Menu` class with TodoService dependency
- Implement methods:
  - `display_main_menu()` - shows options 1-5
  - `display_add_todo_prompts()` - collects title and optional description
  - `display_todos(todos: list[Todo])` - formats and prints todo list
  - `display_update_prompts()` - collects new title and description
  - `display_delete_prompt()` - collects ID and confirms deletion
  - `get_user_choice() -> int` - gets and validates menu selection
  - `run() -> None` - main application loop
- Handle input errors with user-friendly messages

### T-13: Export Menu
- Create `src/ui/__init__.py`
- Export `Menu` class

### T-14: Create main.py entry point
- Create `src/main.py`
- Implement `main()` function:
  - Initialize TodoService
  - Initialize Menu
  - Call Menu.run()
- Add `if __name__ == "__main__":` guard
- Handle KeyboardInterrupt for clean exit

### T-15: Create root __init__.py
- Create `src/__init__.py`
- Leave empty or add package docstring

### T-16: Verify project structure
- Verify pyproject.toml exists and is valid
- Verify all __init__.py files exist
- Verify all .py files exist
- Verify no syntax errors in imports
- Document file list for reference
