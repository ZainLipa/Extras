# Program of the Day: To-Do List

# Initialize an empty to-do list
to_do_list = []

# Function to add a task to the list
def add_task(task):
    to_do_list.append(task)
    print(f"Added '{task}' to the to-do list.")

# Function to view the current to-do list
def view_list():
    if not to_do_list:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(to_do_list, start=1):
            print(f"{index}. {task}")

# Function to remove a task by its index
def remove_task(index):
    if index >= 1 and index <= len(to_do_list):
        removed_task = to_do_list.pop(index - 1)
        print(f"Removed '{removed_task}' from the to-do list.")
    else:
        print("Invalid task index.")

# To-Do List Menu
while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View To-Do List")
    print("3. Remove Task")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        task = input("Enter the task you want to add: ")
        add_task(task)
    elif choice == '2':
        view_list()
    elif choice == '3':
        view_list()
        index = int(input("Enter the index of the task to remove: "))
        remove_task(index)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
