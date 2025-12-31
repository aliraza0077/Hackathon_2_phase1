# Todo In-Memory Console Application - Technical Plan

## 1. Overall Application Flow

```
+----------------------+
|   Application Start  |
+----------+-----------+
           |
           v
+----------------------+
|   Initialize Data    |
|   Store (In-Memory)  |
+----------+-----------+
           |
           v
+----------------------+
|  Display Main Menu   |<------------------+
+----------+-----------+                   |
           |                               |
           v                               |
+----------------------+                   |
|   Get User Input     |                   |
+----------+-----------+                   |
           |                               |
           v                               |
+----------------------+                   |
|   Validate Input     |                   |
+----------+-----------+                   |
           |                               |
           v                               |
    +------+------+                        |
    | Valid?     |                        |
    +-----+------+                        |
          |                               |
      +---+---+                           |
      | Yes |                           |
      +-----+                           |
          |                               |
          v                               |
    +-----+------+                        |
    | Operation  |                        |
    | Handler    |                        |
    +-----+------+                        |
          |                               |
          +------------+------------------+
                       |
                       v
              +--------+--------+
              | Exit?           |
              +--------+--------+
                     |
                +----+----+
                | Yes    |
                +----+----+
                       |
                       v
               +-------+-------+
               |  Exit App    |
               +---------------+
```

**Flow Description:**
1. Application initializes an empty in-memory data structure
2. Main menu loop begins
3. User input is collected and validated
4. Valid input routes to appropriate operation handler
5. Operation executes and returns to main menu
6. Exit option terminates the application

## 2. Console Menu Interaction Flow

### 2.1 Main Menu Display

```
==========================================
           TODO APPLICATION
==========================================

1. Add Todo
2. View All Todos
3. Update Todo
4. Delete Todo
5. Exit

Enter your choice (1-5): _
```

### 2.2 Add Todo Flow

```
1. User selects "Add Todo"
2. Prompt: "Enter todo title: "
3. Prompt: "Enter todo description (optional): "
4. Create todo with generated ID
5. Display confirmation: "Todo added successfully with ID: X"
6. Return to main menu
```

### 2.3 View Todos Flow

```
1. User selects "View All Todos"
2. Clear screen or add separator
3. Display all todos in table format
4. If empty: "No todos found. Add your first todo!"
5. Return to main menu
```

### 2.4 Update Todo Flow

```
1. User selects "Update Todo"
2. Prompt: "Enter todo ID to update: "
3. Validate todo exists
   - If not found: "Error: Todo with ID X not found"
4. Prompt: "Enter new title (leave blank to keep current): "
5. Prompt: "Enter new description (leave blank to keep current): "
6. Update fields if new values provided
7. Display confirmation: "Todo updated successfully"
8. Return to main menu
```

### 2.5 Delete Todo Flow

```
1. User selects "Delete Todo"
2. Prompt: "Enter todo ID to delete: "
3. Validate todo exists
   - If not found: "Error: Todo with ID X not found"
4. Confirm deletion: "Are you sure you want to delete this todo? (y/n): "
5. If confirmed: Remove todo from memory
6. Display confirmation: "Todo deleted successfully"
7. Return to main menu
```

### 2.6 Input Validation Flow

```
+----------------------+
| Get User Input       |
+----------+-----------+
           |
           v
+----------------------+
| Check if empty       |
+----------+-----------+
           |
      +----+----+
      | Empty  | Not Empty
      +----+----+
           |
           v                   v
+----------------------+  +----------------------+
| Display error        |  | Validate format      |
| "Input required"     |  | (number for menu)    |
+----------+-----------+  +----------+-----------+
           |                      |
           |                 +----+----+
           |                 | Valid | Invalid
           |                 +----+----+
           |                      |
           |         +------------+------------+
           |         |                         |
           |         v                         v
           |  +----------------------+  +----------------------+
           |  | Check range          |  | Display error        |
           |  | (1-5 for menu)       |  | "Invalid input"      |
           |  +----------+-----------+  +----------+-----------+
           |             |                      |
           |        +----+----+                 |
           |        | In     | Out of          |
           |        | range  | range           |
           |        +----+----+                |
           |             |                     |
           |             v         +-----------+
           |    +------------------+-----------+
           |    |                              |
           v    v                              v
+----------------------+  +----------------------+
| Execute operation    |  | Display error        |
+----------------------+  | "Invalid choice"     |
                           +----------------------+
```

## 3. Main Components/Modules

### 3.1 Component Diagram

```
src/
├── __init__.py
├── main.py                 # Application entry point
├── models/
│   ├── __init__.py
│   └── todo.py             # Todo data model
├── services/
│   ├── __init__.py
│   └── todo_service.py     # Business logic for todo operations
├── ui/
│   ├── __init__.py
│   └── menu.py             # Console menu and input handling
├── utils/
│   ├── __init__.py
│   └── validators.py       # Input validation functions
└── data/
    ├── __init__.py
    └── todo_store.py       # In-memory data storage
```

### 3.2 Component Responsibilities

| Component | Responsibility |
|-----------|----------------|
| `main.py` | Application entry point, main loop orchestration |
| `models/todo.py` | Todo class definition (ID, title, description, created_at) |
| `services/todo_service.py` | CRUD operations, business logic |
| `ui/menu.py` | Display menus, collect user input, format output |
| `utils/validators.py` | Input validation functions |
| `data/todo_store.py` | In-memory storage container, ID generation |

### 3.3 Data Flow Between Components

```
main.py
    |
    v
menu.py (UI Layer) <---> user input
    |
    v
todo_service.py (Service Layer)
    |
    v
todo_store.py (Data Layer) <---> todo.py (Model)
```

## 4. In-Memory Data Handling Approach

### 4.1 Data Structure

```python
# todos: Dict[int, Todo]
# Key: Auto-incrementing integer ID
# Value: Todo instance
```

### 4.2 ID Generation Strategy

- Use a class-level counter for ID generation
- Counter increments on each new todo
- IDs start at 1 and never reuse deleted IDs
- Simple integer type (no UUID complexity needed)

### 4.3 Todo Class Structure

```python
class Todo:
    id: int
    title: str
    description: str | None
    created_at: datetime
```

### 4.4 Storage Implementation

```python
class TodoStore:
    _todos: dict[int, Todo]
    _next_id: int

    def add(self, todo: Todo) -> int
    def get_all(self) -> list[Todo]
    def get_by_id(self, id: int) -> Todo | None
    def update(self, id: int, **kwargs) -> bool
    def delete(self, id: int) -> bool
```

## 5. Error Handling Strategy

### 5.1 Error Categories

| Category | Example | Handling Approach |
|----------|---------|-------------------|
| Validation | Empty input, invalid number | Display user-friendly message, prompt again |
| Not Found | Invalid todo ID | Display error, return to menu |
| Operation | Delete confirmation declined | No error, return to menu |
| System | Keyboard interrupt | Graceful shutdown |

### 5.2 Error Handling Layers

```
User Input
    |
    v
UI Layer (menu.py)
    - Input validation
    - Format checking
    |
    v
Service Layer (todo_service.py)
    - Business logic validation
    - Entity existence checks
    |
    v
Data Layer (todo_store.py)
    - Storage operations
    - ID generation
```

### 5.3 User Feedback Messages

| Situation | Message |
|-----------|---------|
| Todo added | "Todo added successfully with ID: {id}" |
| Todo updated | "Todo updated successfully" |
| Todo deleted | "Todo deleted successfully" |
| Todo not found | "Error: Todo with ID {id} not found" |
| Invalid input | "Error: Invalid input. Please try again." |
| Empty title | "Error: Title cannot be empty." |
| Delete confirmation declined | "Delete cancelled." |
| Exit confirmation | "Goodbye!" |

### 5.4 Exception Handling

- Use custom exceptions for domain-specific errors
- Catch KeyboardInterrupt (Ctrl+C) for clean exit
- Catch EOFError for piped input scenarios
- Log errors to stderr for debugging

## 6. Project Structure

### 6.1 Directory Layout

```
hackathon2/
├── .plan/
│   └── todo-plan.md
├── .specify/
│   └── todo-spec.md
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── todo.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── todo_service.py
│   ├── ui/
│   │   ├── __init__.py
│   │   └── menu.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── validators.py
│   └── data/
│       ├── __init__.py
│       └── todo_store.py
├── tests/
│   └── (test files)
├── pyproject.toml
├── uv.lock
└── README.md
```

### 6.2 pyproject.toml Configuration

```toml
[project]
name = "todo-app"
version = "0.1.0"
description = "A simple in-memory todo console application"
requires-python = ">=3.13"
dependencies = []

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

### 6.3 Module Imports

```
main.py
  └── imports: menu, todo_service

menu.py
  └── imports: todo_service, validators

todo_service.py
  └── imports: todo, todo_store

todo_store.py
  └── imports: todo, datetime

todo.py
  └── imports: datetime, dataclasses

validators.py
  └── imports: (standard library only)
```

## 7. Implementation Steps Summary

1. Set up project structure with UV
2. Create Todo model (dataclass)
3. Create TodoStore for in-memory data handling
4. Create TodoService for business logic
5. Create validators for input validation
6. Create Menu for UI interactions
7. Create main.py entry point
8. Test application flow

## 8. Quality Standards

- All modules must have docstrings
- Type hints required for function signatures
- Clear separation of concerns
- No external dependencies
- Single responsibility per class/method
