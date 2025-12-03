# task_manager.py
import json
import random
from json import JSONDecodeError
from task import Task


class TaskManager:
    def __init__(self, filename: str = "tasks.json") -> None:
        self.filename = filename
        self.tasks: list[Task] = []
        self.load_from_file()

    # ---------- File Handling ----------

    def load_from_file(self) -> None:
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)

            if isinstance(data, list):
                self.tasks = [Task.from_dict(item) for item in data]
            else:
                self.tasks = []

        except FileNotFoundError:
            self.tasks = []
        except JSONDecodeError:
            print("  Warning: tasks.json file corrupt")
            self.tasks = []
        except Exception as e:
            print(f"  Unexpected error while loading file: {e}")
            self.tasks = []

    def save_to_file(self) -> None:
        try:
            data = [task.to_dict() for task in self.tasks]
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f" Error while saving tasks: {e}")

    # ---------- Helper Methods ----------

    def _generate_id(self) -> int:
        existing_ids = {task.id for task in self.tasks if task.id is not None}
        while True:
            new_id = random.randint(1000, 999999)
            if new_id not in existing_ids:
                return new_id

    def _get_task_by_index(self, index: int) -> Task:
        return self.tasks[index]

    # ---------- CRUD Actions ----------

    def add_task(self, title: str, description: str) -> None:
        task = Task(title=title, description=description)
        task.id = self._generate_id()
        self.tasks.append(task)
        self.save_to_file()
        print("\n Task added successfully!\n")

    def view_tasks(self) -> None:
        if not self.tasks:
            print("\n No tasks found.\n")
            return

        print("\n===== All Tasks =====")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. [{task.id}] {task.title}")
            print(f"   Description : {task.description}")
            print(f"   Created at  : {task.created_at}")
            print("-" * 40)

    def update_task(
        self,
        index: int,
        new_title: str | None = None,
        new_description: str | None = None,
    ) -> None:
        try:
            task = self._get_task_by_index(index)
        except IndexError:
            print("\n Invalid task number. Please try again.\n")
            return

        if new_title:
            task.title = new_title
        if new_description:
            task.description = new_description

        self.save_to_file()
        print("\n Task updated successfully!\n")

    def delete_task(self, index: int) -> None:
        try:
            task = self._get_task_by_index(index)
        except IndexError:
            print("\n Invalid task number. Please try again.\n")
            return

        self.tasks.remove(task)
        self.save_to_file()
        print("\n Task deleted successfully!\n")
