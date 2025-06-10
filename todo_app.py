# Simple To-Do App using Python

tasks = []

def show_menu():
    print("\n📝 To-Do List Menu")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def show_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter the task to add: ")
    tasks.append(task)
    print(f"✅ '{task}' added to your list.")

def remove_task():
    show_tasks()
    if not tasks:
        return
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"❌ '{removed}' removed from the list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program loop
while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("👋 Exiting To-Do App. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
