tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

def uncompleted_task(tasks):
    for task in tasks:
        if task["completed"] == False:
            print(task)

def completed_task(tasks):
    for task in tasks:
        if task["completed"] == True:
            print(task)

def task_descriptions(tasks):
    for task in tasks:
        print(task["description"])

def time_taken(tasks_list, time):
    for task in tasks_list:
        if task["time_taken"] >= time:
            print(task)

def given_description(tasks_list, given_description):
    found = False
    for task in tasks_list:
        if task["description"] == given_description:
            print(task)
            found = True
            break
    if found == False:
        print('error')

def mark_task_complete(tasks_list, given_description):
    found = False
    for task in tasks_list:
        if task["description"] == given_description:
            task["completed"] = True
            found =True
            break
    if found == False:
        print('error')


hoover = {"description": "Hoover", "completed": True, "time_taken": 30 }
def add_new_task(task_list, new_task):
    task_list.append(new_task)



# uncompleted_task(tasks)
# task_descriptions(tasks)
# time_taken(tasks,15)
# given_description(tasks, "Feed C")
# mark_task_complete(tasks, "Feed Cat")
# add_new_task(tasks, hoover)
# print(tasks)

def display_menu():
    while True:
        print("Menu:")
        print("1: Display All Tasks")
        print("2: Display Uncompleted Tasks")
        print("3: Display Completed Tasks")
        print("4: Mark Task as Complete")
        print("5: Get Tasks Which Take Longer Than a Given Time")
        print("6: Find Task by Description")
        print("7: Add a new Task to list")
        print("M or m: Display this menu")
        print("Q or q: Quit")
        choice = (input("what is your choice?: "))
        if choice == "1":
            print(tasks)
        if choice == "2":
            uncompleted_task(tasks)
        if choice == "3":
            completed_task(tasks)
        if choice == "4":
            task_description = input("what is the description of the task you have completed?: ")
            mark_task_complete(tasks, task_description)
        if choice == "5":
            given_time = int(input("Whats the minimum time you would like to spend on this task?: "))
            time_taken(tasks, given_time)
        if choice == "6":
            user_description = input("What is the description of your task?: ")
            given_description(tasks, user_description)
        if choice == "7":
            new_user = {"description": " " , "completed":False , "time_taken": 0 }
            new_user["description"] = input("Description of your new task: ")
            new_user["time_taken"] = int(input("How long does it take to do your task?: "))
            add_new_task(tasks, new_user)
        if choice.lower == "m":
            display_menu()
        if choice.lower == "q":
            break
        else:
            input('option not available, try again: ')

display_menu()