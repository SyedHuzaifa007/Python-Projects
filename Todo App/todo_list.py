import json
import os

name = input("Enter Your Name: ")
print("Welcome", name, "\n")

path = "files/"
os.chdir(path)
print(os.listdir("."))

todo_list = {}
counter = 1

while True:
    user_choice = input("\nPress 1 for adding the task\nPress 2 for editing the task\nPress 3 for removing the task\nPress 4 for displaying the todo list\nPress 5 for exiting the program\n")
    if(user_choice == "1"):
        task_details = input("Enter Your Task Details: ")
        todo_list[counter] = task_details
        counter = counter + 1
    elif (user_choice == "2"):
        task_number = int(input("Enter the Task Number you want to edit: "))
        new_details = input("Enter Your New Task Details: ")
        todo_list[task_number] = new_details
    elif (user_choice == "3"):
        task_number = int(input("Enter the Task Number you want to remove: "))
        todo_list.pop(task_number)
    elif (user_choice == "4"):
        print("TODO List")
        print(todo_list)
    elif (user_choice == "5"):
        file = open(f"files/{name}.json", "w")
        file.write(json.dumps(todo_list))
        file.close()
        print("Thank You for using the TODO App, Have a good day!")
        exit()