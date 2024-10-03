import json
import os

TODO_FILE = "todo_list.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    task_desc = input("Enter task description: ")
    tasks.append({"description": task_desc, "completed": False})
    save_tasks(tasks)
    print(f"Task '{task_desc}' added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{i}. {task['description']} - {status}")

def delete_tasks(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to delete: "))
    if 1 <= task_num <= len(tasks):
        deleted_task = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f"Task '{deleted_task['description']}' deleted successfully!")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Delete Tasks\n4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_tasks(tasks)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
