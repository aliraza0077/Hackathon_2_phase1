"""Todo data model."""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Todo:
    """Represents a single todo item."""

    id: int
    title: str
    description: str | None
    created_at: datetime
