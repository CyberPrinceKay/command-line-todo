import os

# File to store tasks
TASK_FILE = "tasks.txt"

# Ensure task file exists
if not os.path.exists(TASK_FILE):
    with open(TASK_FILE, "w") as file:
        pass


def add_task(task):
    with open(TASK_FILE, "a") as file:
        file.write(f"{task}\n")
    print(f"Task added: {task}")


def view_tasks():
    with open(TASK_FILE, "r") as file:
        tasks = file.readlines()

    if not tasks:
        print("No tasks in the list!")
    else:
        print("Your To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task.strip()}")


def delete_task(task_number):
    with open(TASK_FILE, "r") as file:
        tasks = file.readlines()

    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        with open(TASK_FILE, "w") as file:
            file.writelines(tasks)
        print(f"Removed task: {removed_task.strip()}")
    else:
        print("Invalid task number!")


def main():
    print("Welcome to the Command-Line To-Do List!")
    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("Enter a task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            try:
                task_number = int(input("Enter the task number to delete: "))
                delete_task(task_number)
            except ValueError:
                print("Please enter a valid number!")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again!")


if __name__ == "__main__":
    main()
