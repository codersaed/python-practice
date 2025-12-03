# task.py
from datetime import datetime


class Task:
    def __init__(self, title: str, description: str, created_at: str | None = None):
        self.id: int | None = None 
        self.title = title
        self.description = description

        if created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            self.created_at = created_at

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        task = cls(
            title=data.get("title", ""),
            description=data.get("description", ""),
            created_at=data.get("created_at"),
        )
        task.id = data.get("id")
        return task