"""Todo manager with business logic and console UI."""

from datetime import datetime

from .data import TodoStore
from .models import Todo


class TodoManager:
    """Manages todo operations and console interactions."""

    def __init__(self) -> None:
        self.store = TodoStore()

    def run(self) -> None:
        """Run the main application loop."""
        while True:
            self._display_main_menu()
            choice = self._get_menu_choice()
            if choice == 5:
                self._display_goodbye()
                break
            self._handle_choice(choice)

    def _display_main_menu(self) -> None:
        """Display the main menu."""
        print()
        print("=" * 44)
        print("           TODO APPLICATION")
        print("=" * 44)
        print()
        print("1. Add Todo")
        print("2. View All Todos")
        print("3. Update Todo")
        print("4. Delete Todo")
        print("5. Exit")
        print()

    def _get_menu_choice(self) -> int:
        """Get and validate menu choice from user.

        Returns:
            Valid menu choice (1-5).
        """
        while True:
            try:
                choice = int(input("Enter your choice (1-5): ").strip())
                if 1 <= choice <= 5:
                    return choice
                print("Error: Please enter a number between 1 and 5.")
            except ValueError:
                print("Error: Please enter a valid number.")

    def _handle_choice(self, choice: int) -> None:
        """Handle the user's menu choice."""
        if choice == 1:
            self._add_todo()
        elif choice == 2:
            self._view_todos()
        elif choice == 3:
            self._update_todo()
        elif choice == 4:
            self._delete_todo()

    def _add_todo(self) -> None:
        """Add a new todo."""
        print()
        print("--- Add Todo ---")

        title = self._get_non_empty_input("Enter todo title: ")
        description = input("Enter todo description (optional): ").strip()
        description = description if description else None

        todo = Todo(
            id=0,  # ID will be assigned by store
            title=title,
            description=description,
            created_at=datetime.now(),
        )

        todo_id = self.store.add(todo)
        print(f"Todo added successfully with ID: {todo_id}")

    def _view_todos(self) -> None:
        """Display all todos."""
        print()
        print("--- All Todos ---")
        print()

        todos = self.store.get_all()

        if not todos:
            print("No todos found. Add your first todo!")
            return

        for todo in todos:
            self._display_todo(todo)

        print(f"\nTotal: {len(todos)} todo(s)")

    def _display_todo(self, todo: Todo) -> None:
        """Display a single todo."""
        print(f"ID: {todo.id}")
        print(f"Title: {todo.title}")
        if todo.description:
            print(f"Description: {todo.description}")
        print(f"Created: {todo.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 40)

    def _update_todo(self) -> None:
        """Update an existing todo."""
        print()
        print("--- Update Todo ---")

        todo_id = self._get_todo_id()
        if todo_id is None:
            return

        todo = self.store.get_by_id(todo_id)

        new_title = input("Enter new title (leave blank to keep current): ").strip()
        new_description = input("Enter new description (leave blank to keep current): ").strip()

        updates = {}
        if new_title:
            updates["title"] = new_title
        if new_description:
            updates["description"] = new_description

        if not updates:
            print("No changes made.")
            return

        self.store.update(todo_id, **updates)
        print("Todo updated successfully.")

    def _delete_todo(self) -> None:
        """Delete a todo."""
        print()
        print("--- Delete Todo ---")

        todo_id = self._get_todo_id()
        if todo_id is None:
            return

        todo = self.store.get_by_id(todo_id)
        print(f"Selected: {todo.title}")

        confirm = self._get_yes_no("Are you sure you want to delete this todo? (y/n): ")
        if not confirm:
            print("Delete cancelled.")
            return

        self.store.delete(todo_id)
        print("Todo deleted successfully.")

    def _get_non_empty_input(self, prompt: str) -> str:
        """Get non-empty input from user.

        Args:
            prompt: The input prompt to display.

        Returns:
            Non-empty input string.
        """
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("Error: This field cannot be empty.")

    def _get_todo_id(self) -> int | None:
        """Get a valid todo ID from user.

        Returns:
            The todo ID if found, None if cancelled.
        """
        while True:
            try:
                todo_id = int(input("Enter todo ID: ").strip())
                if todo_id <= 0:
                    print("Error: Please enter a positive number.")
                    continue

                if self.store.get_by_id(todo_id) is None:
                    print(f"Error: Todo with ID {todo_id} not found.")
                    return None

                return todo_id
            except ValueError:
                print("Error: Please enter a valid number.")

    def _get_yes_no(self, prompt: str) -> bool:
        """Get yes/no confirmation from user.

        Args:
            prompt: The confirmation prompt.

        Returns:
            True for 'y' or 'Y', False for 'n' or 'N'.
        """
        while True:
            response = input(prompt).strip().lower()
            if response in ("y", "yes"):
                return True
            elif response in ("n", "no"):
                return False
            print("Error: Please enter 'y' or 'n'.")

    def _display_goodbye(self) -> None:
        """Display goodbye message."""
        print()
        print("Goodbye!")
