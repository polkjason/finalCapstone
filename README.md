# finalCapstone

## Description and Purpose of the Project
This repository is a duplicate of the Task_Manager repository, and is being used for my HyperionDev Bootcamp assignment to show the final capstone project using the name requested
in the assignment. It also features pull requests to resolve two issues.

## Installation
This project requires the python runtime executable. Compile and run the project on whatever IDE you prefer.

## Usage
When the project starts, you will be prompted for login credentials. To log in as an administrator, use username: admin and password: password. You then be presented with a menu displaying the main menu based on user priviliges-- in the case of the screenshots, admin.


![image](https://github.com/polkjason/finalCapstone/assets/61259810/81cbea79-4c7a-4f44-8851-39c256a4522e)

### Main Menu
r: Select this option to create a new user

![image](https://github.com/polkjason/finalCapstone/assets/61259810/440fe38e-b10b-499a-8482-6669151b53ad)

a: Select this to add a task and assign it to an existing user. A due must also be assigned. The program ensures the due is greater than the current date.

![image](https://github.com/polkjason/finalCapstone/assets/61259810/6baedb11-4d18-4b11-80da-0416f92c0ad6)

va: Select this option to view all tasks for every user. This will also display the details for each task, including if completed and if overdue.

![image](https://github.com/polkjason/finalCapstone/assets/61259810/768e4972-f1f7-4058-9a68-903cd43796e0)

vm: Select this option to view your own tasks. All tasks assigned to you will display. Use the task ID to select the task to either mark it complete, reassign to another user, or change the due date. If a new user is assigned the task, then the task will need to be given a new due date.

![image](https://github.com/polkjason/finalCapstone/assets/61259810/a3b3dab8-859a-44e1-b3d4-8badc914662e)
![image](https://github.com/polkjason/finalCapstone/assets/61259810/594391f1-9902-4552-81e5-2a556f7d70bb)

e: exits the program.

![image](https://github.com/polkjason/finalCapstone/assets/61259810/bd4511e2-f7e3-4a8f-8b77-2fd102b319e9)

#### Admin only Main Menu Options:
gr: Select this option to generate reports for all tasks and write them to two files.

##### task_overview.txt
This file holds the total tasks, total completed, total incompleted, and total overdue. Further, it has percentage incompleted and it has percentage of tasks overdue.

##### user_overview.txt
This file holds details for each user's specific tasks. It also has the total completed, incompleted, and overdue as well as the percentages for each.

ds: Select this to generate the same statistics that gr creates, but instead of outputting the information to a file, it is displayed to the terminal window.

## Credits
Author: Jason Polk (https://github.com/polkjason)
