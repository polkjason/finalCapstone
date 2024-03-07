# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.
#Functionality extended to allow tasks to be editted, reports to be generated (generate reports to file), and statistics to be displayed (generate reports to screen.)
#Separated many bulky functions to separate tasks with attempts to decouple functions as much as possible without refactoring for OOP
#priority_fixes.txt and RequirementsParkingLot.txt added to give further details to the design of the application as well as the direction of future development.

#Statistics and Reports:
#Completed tasks are tasks that were marked completed regardless of whether they were overdue or not.
#Incomplete tasks are tasks that are marked as incomplete
#Overdue tasks are tasks that are marked incomplete and the due date has passed. Completed overdue tasks
#are not grouped with overdue tasks as they are completed tasks. 

#Task Note: The tasks do not define what "overdue" means, so my interpretation is past due and incomplete.

#Task Note: I tried to code the project as closely to the use cases of the tasks as possible to prevent
#scope creep. Example: va printing ovrdue tasks was not defined in the tasks so I would not have included that feature.

#Task Note: I did eliminated the the task_id unused variable, but I was unable to find the variables that were noted as being unused on lines 477 to 484.
#I added code before looking for them, so I'm not sure where they would be located now or what the variable names are.

#Task Note: I didn't put the log-in portion of the code in a function because the task didn't request that of me. I tried to follow the task
#requirements as closely as I could. TBH, I would have preferred to do all of this using OOP, but the task requested proceduaral programming instead.

#Task Note: Also, plese bear in mind that I turned this assignment in quite early on in the bootcamp. If the assignment details have been changed since, then
#I would not have been privvy to them as the changes would have likely been made after my submission in late December/ early January.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

#Display the menu depending on access rights.
#admin only can generate reports and display statistics.
def display_menu():
    # making sure that the user input is converted to lower case.
    print()
    if(curr_user == 'admin'):
        menu = input('''Select one of the following Options below:
            r - Registering a user
            a - Adding a task
            va - View all tasks
            vm - View my task
            gr = Generate Reports
            ds - Display statistics
            e - Exit
            : ''').lower()
    
    else:

        menu = input('''Select one of the following Options below:
                        r - Registering a user
                        a - Adding a task
                        va - View all tasks
                        vm - View my task
                        e - Exit
                        : ''').lower()
    return menu

#searches user.txt for the specified user using a simple linear search method.
def search_users(search_item):
    with open("user.txt", 'r') as user_file:
        #read all the lines of the file at once.
        lines = user_file.readlines()

        #for each line in the file
        for l in lines:
            #strip away all the trash characters, such as newline and EOF
            l = l.strip()
            #split the line delimited by ';' and access the first array element to compare
            #against search_item.
            if(l.split(';')[0] == search_item):
                return True
        
        return False

#add a new user.        
def reg_user(user_data):
    '''Add a new user to the user.txt file'''
    # - Request input of a new username
    new_username = input("New Username: ")

    user_exists = search_users(new_username)
    while(user_exists):
        if(user_exists):
            if(new_username.lower() == "admin"):
                print("admin is a disallowed Username. Please type a new Username: ")
            else:
                print("Username already exist. Please type a new Username: ")
            new_username = input("New Username: ")
        
        user_exists = search_users(new_username)

    # - Request input of a new password
    new_password = input("New Password: ")

    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file,
        print("New user added")
        username_password[new_username] = new_password
            
        with open("user.txt", "w") as out_file:
            #Next line is important to prevent duplicates being written to file
            user_data = [] 
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))


    # - Otherwise you present a relevant message.
    else:
        print("Passwords do no match")

#add a new task.
def add_task(task_list):
    '''Allow a user to add a new task to task.txt file
        Prompt a user for the following: 
        - A username of the person whom the task is assigned to,
        - A title of a task,
        - A description of the task and 
        - the due date of the task.'''
    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        return    #Was meant to make program continue loop from error. Not sure if still needed somewhere.#############
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            done = False
            while(done != True):
                task_due_date = input("Due date of task (YYYY-MM-DD): ")
                due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                if(due_date_time > datetime.today()):
                    done = True
                else:
                    print("Cannot set the due date for a task if the due date has already past.")
                    print("Please enter a new due date.")
                
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")


    # Then get the current date.
    curr_date = date.today()
    
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''

    #Count number of task this user already has and assign a task ID accordingly
    task_count = count_tasks()

    #create a new task object to be written to tasks.txt
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False,
        "task_id": str(task_count + 1),
        "overdue": False
    }

    #first, add the new task to the task list using the append method.
    task_list.append(new_task)
    #them write the entire task list to tasks.txt
    #overwriting whatever was there previously.
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No",
                t['task_id'],
                "Yes" if t['overdue'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")

#view all tasks.
def view_all():
    '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling) 
    '''

    #create the string piece by piece, then display.
    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        if(t['completed'] == True):
            disp_str += "Completed: Yes\n"
        else:
            disp_str += "Completed: No\n"
        if(t['overdue'] == True):
            disp_str += "Overdue: Yes\n"
        else:
            disp_str += "Overdue: No\n"
        print(disp_str)

#seaches the task list for the specified task by task_id.
#simple linear search
def find_user_task_by_id(task_search_id):
    for t in task_list:
        if(t['username'] == curr_user) and (t['task_id'] == task_search_id):
            return t

    return {"username": ""}

#view all tasks for the currently logged in user.
def view_mine():
    '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
    '''

    print(f"Now viewing {count_user_tasks(curr_user)} task(s) for {curr_user}: \n")

    for t in task_list:
        if t['username'] == curr_user:
            if(t['completed']):
                task_completed_string = "Yes"
            else:
                task_completed_string = "No"

            disp_str = f"Task ID: \t {t['task_id']}\n"
            disp_str += f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            disp_str += f"Task Completed: \t {task_completed_string}\n"
            print(disp_str)
            

    """
    Allow user to view details of a task by typing the task number. -1 quits back to main menu.
    """
    task = {"username": ""}
    done = False
    while(task['username'] == "" and done == False):
        task_id_input = input("Please type the number corresponding to the task ID you would like to edit. -1 to quit to main menu: ")
        if(int(task_id_input) == -1):
            done = True
        else:
            task = find_user_task_by_id(task_id_input)
            if(task['username'] == ""):
                print("Task ID not found. Please enter a valid task ID to edit its details.")
            else:
                display_task(task)
                edit_task(task, int(task_id_input))
                task = {"username": ""}

#edit a selected task                                
def edit_task(task, task_id):
    display_edit_task_menu()
    menu_input = input("Please enter your selection: ")

    #task['completed'] holds boolean values despite being recorded to tasks.txt as Yes/No
    #Must check True for Yes and False for No

    #change assigned user
    if(menu_input == "1"):
        if(task['completed'] == False):
            edit_task_change_task_username_menuitem(task, task_id)
        else:
            print("Cannot change the person assigned to a task when the task assigned has been marked completed.")
    #change the due date of the task        
    elif(menu_input == "2"):
        if(task['completed'] == False):
            edit_task_change_due_date_menuitem(task, task_id)
        else:
            print("Cannot change the due date of a task that has been marked completed.")
    #mark the task completed
    elif(menu_input == "3"):
            edit_task_mark_completed_menuitem(task, task_id)
    #return to previous menu        
    elif(menu_input == "-1"):
        return task
    #catch input that is other what is expected    
    else:
        print("The option selected is not on the menu.")

    return task

#marks the task as completed
def edit_task_mark_completed_menuitem(task, task_id):
    print("Should this task be marked complete?")
    completion_input = input("Please enter 'yes' to mark as complete and 'no' to mark it incomplete. Any other input will return to task selction: ")

    if(completion_input.lower() == "yes"):
        task['completed'] = True
        
        update_task_file()
        print("Task marked as complete.")
        
    elif(completion_input.lower() == "no"):
        task['completed'] = False
       
        update_task_file()
        print("Task marked as incomplete")
        
    else:
        print("Please enter either yes or no to mark task completion.")

    print("Returning to task selection menu.")
    return task

#change the assigned username, forces update of due date if earlier than current date
def edit_task_change_task_username_menuitem(task):
    username_input = input("Please enter the username of the person to assign to this task: ")

    #Make sure username exists first
    if username_input not in username_password.keys():
        print("User does not exist. Please enter a valid username")
    else:

        task['username'] = username_input

        # Then get the current date.
        curr_date = date.today()
        task['assigned_date'] = curr_date

        #make sure the due date is not less than the assignment date. If so then inform user they will now change the due date of the task.
        due_date = task['due_date'].date()
        if(due_date < curr_date):
            print(f"Due date of {task['title']} task {due_date} is now set before the assignment date {curr_date} for username {task['username']}.")
            print(f"Please update the task due date now.")
            
            edit_task_change_due_date_menuitem(task, task_id)        

        update_task_file()

        print("Username has been updated.")

    print("Returning to task edit menu.")    
    return task

#change due date of task
def edit_task_change_due_date_menuitem(task, task_id):
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)

            assigned_date = task['assigned_date'].strftime(DATETIME_STRING_FORMAT)
            assigned_date = datetime.strptime(assigned_date, DATETIME_STRING_FORMAT)

            print(f"Assigned date: {assigned_date}, Due date: {due_date_time}")
            if(due_date_time < assigned_date):
                print("The due date of the task must be equal to or after the assigned date.")
            else:
                task['due_date'] = due_date_time
                update_task_file()
                break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")
    return task

#display the edit task menu
def display_edit_task_menu():
    print("Edit Task")
    print("The username assigned to the task and the task's due date cannot be editted if the task is marked complete.")
    print("Select from the following edit options.")
    print("1) Type 1 to change username of the person assigned to this task.")
    print("2) Type 2 to change the due date of the task")
    print("3) Type 3 to mark a task as either completed or not completed.")
    print("Type -1 to quit back to the main menu.")

#display specified task
def display_task(task):
    if(task['completed']):
        task_completed_string = "Yes"
    else:
        task_completed_string = "No"
    print()
    disp_str = f"Task ID: \t {task['task_id']}\n"
    disp_str += f"Task: \t\t {task['title']}\n"
    disp_str += f"Assigned to: \t {task['username']}\n"
    disp_str += f"Date Assigned: \t {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
    disp_str += f"Due Date: \t {task['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
    disp_str += f"Task Description: \n {task['description']}\n"
    disp_str += f"Task Completed: \t {task_completed_string}\n"
    print(disp_str)

#update the tasks.txt by writing task_list to the file
def update_task_file():
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No",
                t['task_id'],
                "Yes" if t['due_date'] > datetime.today() else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))

#count the number of tasks in task_list
def count_tasks():
    task_count = 0
    for t in task_list:
        task_count += 1
    return task_count

#count the total tasks marked as completed in task_list
def count_completed_tasks():
    completed_count = 0
    for t in task_list:
        if(t['completed'] == True):
            completed_count += 1
    return completed_count

#count the total tasks marked as incompleted in task_list
def count_incomplete_tasks():
    incompleted_count = 0
    for t in task_list:
        if(t['completed'] == False):
            incompleted_count += 1
    return incompleted_count

#count the total tasks marked as incompleted and overdue
def count_overdue_tasks():
    overdue_count = 0
    for t in task_list:
        if(t['completed'] == False):
            curr_date = date.today()
            
            if(curr_date > t['due_date'].date()):
                overdue_count += 1
    return overdue_count

#Used by both "display statistics" and "generate reports" to get the information needed for these statistics.
def create_tasks_overview_report():
    task_count = count_tasks()
    competed_task_count = count_completed_tasks()
    incompleted_task_count = count_incomplete_tasks()
    overdue_task_count = count_overdue_tasks()
    write_to_file = ""

    incomplete_percentage = (incompleted_task_count / task_count) * 100
    overdue_percentage = (overdue_task_count / task_count) * 100

    write_to_file += f"Total tasks: {task_count} \n" 
    write_to_file += f"Tasks Complete: {competed_task_count} \n" 
    write_to_file += f"Tasks Incomplete: {incompleted_task_count} \n" 
    write_to_file += f"Tasks Overdue: {overdue_task_count} \n \n" 
    write_to_file += f"Percentage of Tasks Incomplete: {incomplete_percentage} \n" 
    write_to_file += f"Percentage of Tasks Overdue: {overdue_percentage}" 

    return write_to_file                

#count the number of tasks assigned to a specified user.
def count_user_tasks(username):
    user_task_count = 0
    for t in task_list:
        if(username == t['username']):
            user_task_count += 1
    return user_task_count

#count total tasks completed by a specified user
def count_user_completed_tasks(username):
    completed_count = 0
    for t in task_list:
        if(t['completed'] == True and username == t['username']):
            completed_count += 1
    return completed_count

#count the number of incompleted tasks assigned to a specified user
def count_user_incompleted_tasks(username):
    incompleted_count = 0
    for t in task_list:
        if(t['completed'] == False and username == t['username']):
            incompleted_count += 1
    return incompleted_count

#count the number of tasks assigned to a specified user that
#are marked incompleted and overdue
def count_user_overdue_tasks(username):
    overdue_count = 0
    for t in task_list:
        if(t['completed'] == False and username == t['username']):
            curr_date = date.today()
            if(curr_date > t['due_date'].date()):
                overdue_count += 1
    
    return overdue_count

#Used by both "display statistics" and "generate reports" to get the information needed for these statistics.
def create_users_overview_report():
    task_count = count_tasks()
    user_task_count = 0
    user_completed_task_count = 0
    user_incompleted_task_count = 0
    user_overdue_task_count = 0
    user_percentage_of_total_tasks = 0
    user_percentage_task_completed = 0
    user_percentage_task_incompleted = 0
    user_percentage_task_overdue = 0

    write_to_file = ""

    
    for user in user_data:
        username = user.split(';')[0] #Get just the username from each user entry
        user_task_count = count_user_tasks(username)
        user_completed_task_count = count_user_completed_tasks(username)
        user_incompleted_task_count = count_user_incompleted_tasks(username)
        user_overdue_task_count = count_user_overdue_tasks(username)

        if(user_task_count != 0):
            user_percentage_of_total_tasks = (user_task_count / task_count) * 100
            user_percentage_task_completed = (user_completed_task_count / user_task_count) * 100
            user_percentage_task_incompleted = (user_incompleted_task_count / user_task_count) * 100
            user_percentage_task_overdue = (user_overdue_task_count / user_task_count) * 100
        else:
            user_percentage_of_total_tasks = 0
            user_percentage_task_completed = 0
            user_percentage_task_incompleted = 0
            user_percentage_task_overdue = 0

        write_to_file += f"User: {username} \n" 
        write_to_file += f"Total Tasks Assigned to User: {user_task_count} \n" 
        write_to_file += f"Percentage of Total Tasks Assigned to {username}: {user_percentage_of_total_tasks} \n" 
        write_to_file += f"Percentage of {username}'s Tasks Completed: {user_percentage_task_completed} \n" 
        write_to_file += f"Percentage of {username}'s Tasks Incompleted: {user_percentage_task_incompleted} \n" 
        write_to_file += f"Percentage of {username}'s Tasks Overdue: {user_percentage_task_overdue} \n \n"
    return write_to_file    

#Creates two text files, task_overview.txt and user_overview.txt.
# task_overview stores summary stats about the tasks such as overdue tasks, completed tasks, incomplete tasks
# user_overview stores summary stats about each user's tasks, completed, incompleted, overdue     
def generate_reports():
    print("Creating task_overview.txt...")
    write_to_file = create_tasks_overview_report()
    with open("task_overview.txt", "w") as to_file:
        to_file.write(write_to_file)
    print("Done")
    print("Creating user_overview.txt...")
    write_to_file = create_users_overview_report()
    with open("user_overview.txt", "w") as uo_file:
        uo_file.write(write_to_file)
    print("Done")

def display_statistics():
    '''If the user is an admin they can display statistics about number of users
        and tasks.'''
    num_users = len(username_password.keys())
    num_tasks = len(task_list)

    print("-----------------------------------")
    print(f"Number of users: \t\t {num_users}")
    print(f"Number of tasks: \t\t {num_tasks}")
    print("-----------------------------------")

    display_task_statistics_string = create_tasks_overview_report()
    display_user_task_statistics_string = create_users_overview_report()

    print("Task Summary Statistics")
    print(display_task_statistics_string)
    print("-----------------------------------")
    print("Task Summary Statistics Per User")
    print(display_user_task_statistics_string)
    print("-----------------------------------")


# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False
    curr_t['task_id'] = task_components[6]
    curr_t['overdue'] = True if task_components[7] == "Yes" else False

    task_list.append(curr_t)

#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")
    
# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and 
    menu = display_menu()
    
    

    if menu == 'r':
        reg_user(user_data)

    elif menu == 'a':
        add_task(task_list)

    elif menu == 'va':
        view_all()       

    elif menu == 'vm':
        view_mine()

    elif menu == 'gr' and curr_user == 'admin':
        generate_reports()
        
    elif menu == 'ds' and curr_user == 'admin': 
        display_statistics()    

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")