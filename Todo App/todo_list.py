name = input("Enter Your Name: ")
print("Welcome", name, "\n")
file = open("todo_list.txt", "r")
content = file.read()
content_found = [x.split(",") for x in content]
print(content_found)
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
        file = open("todo_list.txt", "a")
        file.write(name)
        file.write(",")
        file.write(str(todo_list))
        file.write("\n")
        file.close()
        print("Thank You for using the TODO List, Have a good day!")
        exit()