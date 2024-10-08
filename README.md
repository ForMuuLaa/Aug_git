    task = {} # my global varaible for global access to hold my tasks


Displays the main menu options for the user to interact with the application.
Add Task Function
    
    def menu(): 
        print("-------------------------------------------")
        print("Menu:")
        print("-------------------------------------------")
        print("1. add-task")
        print("2. view-tasks")
        print("3. mark-completed")
        print("4. delete-task")
        print("5. Quit")
        print("-------------------------------------------")

Purpose: Allows users to add new tasks to their list.
User Prompt: Asks the user for a task name or 'done' to exit.
Duplicate Check: Informs the user if the task already exists.
Task Addition: Adds new tasks marked as 'Incomplete'.
Final Output: Displays a decorative line and checks if tasks are present.
    
    def add_task():
        global task  # Declare that we are using the global variable 'task'
        print("What task would you like to add? Enter 'done' to go back.\n")
        
    while True:
        user_input = input().strip()  # Get user input and strip whitespace
        if user_input.lower() == 'done':# Check if the user wants to exit the adding process
            break
        if task.get(user_input):# Check if the task already exists in the dictionary
            print(f"Task '{user_input}' already exists.")  # Inform user if task is a duplicate
        else:
            # Add the new task as 'Incomplete'
            task.update({user_input: 'Incomplete'})
    
    print("\n-------------------------------------------")  # Decorative line for output separation
    
    # Check if the task dictionary is empty and display tasks if it's not
    if not task:  
        view_tasks()
        
Purpose: Displays the current list of tasks and their completion statuses.
Check for Tasks: Informs the user if no tasks are available.
Task Display: Prints each task in a neat format showing its status.
Return Value: Returns the current task dictionary.

    def view_tasks():
        global task
        if not task:#checks if task is empty
             print("You have no tasks at the moment.")
        for key, value in task.items(): #prints out tasks neatly
            print(f"{key}: {value}")
        return task 

Purpose: Allows users to mark tasks as completed.
Check for Tasks: Informs the user if no tasks are available.
User Input: Prompts for the task name to mark complete or 'done' to exit.
Completion Logic:
Informs if the task does not exist or is already completed.
Marks the task as completed if it exists and is not yet completed.
Final Update: Displays the updated list of tasks after marking.

    def mark_complete():
        global task  # Declare that we are using the global variable 'task'
        if not task:# Check if the task dictionary is empty
            print("You have no tasks at the moment.")
        else:
            view_tasks()  # Display current tasks
            print("Which task would you like to mark as completed? Enter 'done' to go back.")
    
        while True:
            if not task:  # If tasks are empty during the loop, break out
                break
            user_input = input().strip()  # Get user input and strip whitespace
            if user_input.lower() == 'done':# Check if user wants to exit the marking process
                break
            # Check if the user_input exists in the task dictionary
            if not task.get(user_input):
                print("Error: Your task does not yet exist.")  # Inform user if task is not found
            elif task.get(user_input) == 'Completed':
                print(f"Your task '{user_input}' is already completed.")  # Inform user if task is already completed
            else:
                # Mark the task as completed
                task.update({user_input: 'Completed'})
                print(f'Your task "{user_input}" has been marked as completed.')
        
        print("\n-------------------------------------------")  # Decorative line for output separation
        view_tasks()  # Display remaining tasks after marking

Purpose: Allows users to delete tasks from their list.
Check for Tasks: Informs the user if no tasks are available.
User Input: Prompts for the task name to delete or 'done' to exit.
Deletion Logic:
Removes the task if it exists, or informs the user if it does not.
Final Update: Displays the updated list of tasks after deletion.

    def delete_task():
    
        global task  # Declare that we are using the global variable 'task'
        # Check if the task dictionary is empty
        if not task:
            print("You have no tasks at the moment.")
        else:
            view_tasks()  # Display current tasks
            print("Which task would you like to delete? Enter 'done' to go back")
        while True:
            if not task:  # If tasks are empty during the loop, break out
                break
            user_input = input().strip()  # Get user input and strip whitespace
            if user_input.lower() == 'done':# Check if user wants to exit the deletion process
                break
            # Check if the user_input exists in the task dictionary
            elif task.get(user_input):
                task.pop(user_input)  # Remove the task from the dictionary
                print(f"Task '{user_input}' has been removed.")
            else:
                # Inform the user if the task does not exist
                print(f"This '{user_input}' task does not yet exist.")
        
        view_tasks()  # Display remaining tasks after deletion
   
Calls the menu() function to show available options for task management.
User Input Handling: Captures and processes user input, ensuring whitespace is stripped for accurate comparison.
Option Handling:

Option 5: Exits the loop, terminating the application.
Option 1: Calls add_task() to add a new task.
Option 2: Calls view_tasks() to display existing tasks.
Option 3: Calls mark_complete() to mark a selected task as completed.
Option 4: Calls delete_task() to remove a task from the list.
Error Handling: Provides feedback for invalid input, prompting the user to enter a valid option from the menu.

    while True:
        menu()  # Display the menu options to the user
        user_input = input('* Please enter in a number *: ').strip()  # Get user input and strip whitespace
        
        # Exit the loop if the user chooses option 5
        if user_input == '5':
            break
        # Handle the selection for adding a task
        elif user_input == '1':
            back = 1  # Set back variable to indicate the action taken
            add_task()  # Call the function to add a new task
        # Handle the selection for viewing tasks
        elif user_input == '2':
            view_tasks()  # Call the function to display current tasks
        # Handle the selection for marking a task as complete
        elif user_input == '3':
            back = 3  # Set back variable to indicate the action taken
            mark_complete()  # Call the function to mark a task as completed
        # Handle the selection for deleting a task
        elif user_input == '4':
            back = 4  # Set back variable to indicate the action taken
            delete_task()  # Call the function to delete a task
        # Handle invalid input
        else:
            print('Error: please enter one of the choices listed (1, 2, 3, 4, 5)')
    

