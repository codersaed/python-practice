# main.py
from task_manager import TaskManager

def show_menu() -> None:
    print("===== Student Task Tracker =====")
    print("1. Add New Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def main() -> None:
    manager = TaskManager()

    while True:
        show_menu()
        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            # Add new task
            title = input("Task Title: ").strip()
            description = input("Description: ").strip()

            if not title:
                print(" Title can not be empty.\n")
                continue

            manager.add_task(title, description)

        elif choice == "2":
            # View all tasks
            manager.view_tasks()

        elif choice == "3":
            # Update task
            if not manager.tasks:
                print("\n No tasks to update.\n")
                continue

            manager.view_tasks()
            try:
                num = int(input("Enter task number to update: ").strip())
                index = num - 1
            except ValueError:
                print("\n Please enter a valid number.\n")
                continue

            new_title = input("New title (blank = keep same): ").strip()
            new_desc = input("New description (blank = keep same): ").strip()

            manager.update_task(
                index,
                new_title if new_title else None,
                new_desc if new_desc else None,
            )

        elif choice == "4":
            # Delete task
            if not manager.tasks:
                print("\n No tasks to delete.\n")
                continue

            manager.view_tasks()
            try:
                num = int(input("Enter task number to delete: ").strip())
                index = num - 1
            except ValueError:
                print("\n Please enter a valid number.\n")
                continue

            manager.delete_task(index)

        elif choice == "5":
            # Exit
            print("\n Saving tasks and exiting... Bye!\n")
            manager.save_to_file()
            break

        else:
            print("\n Invalid choice. Please select between 1 and 5.\n")


if __name__ == "__main__":
    main()
