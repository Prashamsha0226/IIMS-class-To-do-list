# Function to display the to-do list
def display_todo_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("Your To-Do List:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")

# Function to add a task to the to-do list
def add_task(todo_list, task):
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")

# Function to remove a task from the to-do list
def remove_task(todo_list, task_index):
    try:
        removed_task = todo_list.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from the list.")
    except IndexError:
        print("Invalid task number. Please try again.")

# Function to mark a task as completed (optional)
def mark_completed(todo_list, task_index):
    try:
        task = todo_list[task_index - 1]
        todo_list[task_index - 1] = f"{task} - Completed"
        print(f"Task '{task}' marked as completed.")
    except IndexError:
        print("Invalid task number. Please try again.")

# Main function to handle user input
def main():
    todo_list = []

    while True:
        print("\nTo-Do List Options:")
        print("1. Display to-do list")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Mark a task as completed")
        print("5. Exit")

        # Taking user input for the action
        choice = input("Enter the number corresponding to the action: ")

        if choice == "1":
            # If the user chooses to display the to-do list
            display_todo_list(todo_list)
        elif choice == "2":
            # If the user chooses to add a task
            task = input("Enter the task you want to add: ")
            add_task(todo_list, task)
        elif choice == "3":
            # If the user chooses to remove a task
            display_todo_list(todo_list)
            try:
                task_index = int(input("Enter the task number to remove: "))
                remove_task(todo_list, task_index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "4":
            # If the user chooses to mark a task as completed
            display_todo_list(todo_list)
            try:
                task_index = int(input("Enter the task number to mark as completed: "))
                mark_completed(todo_list, task_index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "5":
            # If the user chooses to exit the application
            print("Exiting the to-do list application.")
            break
        else:
            # If the user enters an invalid option
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
