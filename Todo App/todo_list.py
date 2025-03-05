import json
import os

name = input("Enter Your Name: ")
print("Welcome", name, "\n")

files = []

global counter
global previous_todo_dict

files = os.listdir(".")

if name + ".json" in files:
    print("JSON found")
    previous_list = open(name + ".json", "r")
    previous_todo_dict = json.load(previous_list)
    print(previous_todo_dict)
    counter = len(previous_todo_dict) + 1
else:
    print("No JSON found")
    counter = 1
    previous_todo_dict = {}

todo_list = previous_todo_dict

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
        todo_list.pop(str(task_number))
    elif (user_choice == "4"):
        print("TODO List")
        print(todo_list)
    elif (user_choice == "5"):
        renumbered_todo_list = {str(i + 1): task for i, task in enumerate(todo_list.values())}
        file = open(f"{name}.json", "w")
        file.write(json.dumps(renumbered_todo_list))
        file.close()
        print("Thank You for using the TODO App, Have a good day!")
        exit()