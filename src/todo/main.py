"""Todo application entry point."""

from .manager import TodoManager


def main() -> None:
    """Run the todo application."""
    try:
        manager = TodoManager()
        manager.run()
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
    except EOFError:
        print("\n\nGoodbye!")


if __name__ == "__main__":
    main()
