"""In-memory todo storage."""

from typing import Any

from ..models import Todo


class TodoStore:
    """In-memory storage for todo items."""

    def __init__(self) -> None:
        self._todos: dict[int, Todo] = {}
        self._next_id: int = 1

    def add(self, todo: Todo) -> int:
        """Add a todo and return its assigned ID.

        Args:
            todo: The todo to add.

        Returns:
            The unique ID assigned to the todo.
        """
        todo_id = self._next_id
        self._next_id += 1
        todo.id = todo_id
        self._todos[todo_id] = todo
        return todo_id

    def get_all(self) -> list[Todo]:
        """Return all todos sorted by ID.

        Returns:
            List of all todos in ID order.
        """
        return sorted(self._todos.values(), key=lambda t: t.id)

    def get_by_id(self, todo_id: int) -> Todo | None:
        """Retrieve a todo by its ID.

        Args:
            todo_id: The ID to look up.

        Returns:
            The todo if found, None otherwise.
        """
        return self._todos.get(todo_id)

    def update(self, todo_id: int, **kwargs: Any) -> bool:
        """Update fields of an existing todo.

        Args:
            todo_id: The ID of the todo to update.
            **kwargs: Fields to update (title, description).

        Returns:
            True if the todo was found and updated, False otherwise.
        """
        todo = self._todos.get(todo_id)
        if todo is None:
            return False

        if "title" in kwargs:
            todo.title = kwargs["title"]
        if "description" in kwargs:
            todo.description = kwargs["description"]

        return True

    def delete(self, todo_id: int) -> bool:
        """Delete a todo by its ID.

        Args:
            todo_id: The ID of the todo to delete.

        Returns:
            True if the todo was found and deleted, False otherwise.
        """
        if todo_id not in self._todos:
            return False

        del self._todos[todo_id]
        return True
