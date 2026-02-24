def add_task(tasks_list):
    # gets all values from user
    task_id = len(tasks_list)+1
    while True:
        task_title = input("Print task title: ")
        if not task_title:
            print("You can NOT add task without title!") # checks if title is empty
            continue
        else:
            break
    task_done = False
    while True:
        task_priority = input("Choose priority (high, medium, low): ").lower()
        if not (task_priority=="high" or task_priority=="medium" or task_priority=="low"):
            print("Invalid input!")  #if enter different words than given ones, can't continue
            continue
        else:
            break
    tags = input("Enter the task tags: ")
    task_tags = tags.replace(",", " ")
    # adds all values to dictionary
    task={
        "ID": task_id,
        "Title": task_title,
        "Done": task_done,
        "Priority": task_priority,
        "Tags": task_tags.split()
    }
    #adds new dictionary to task list
    tasks_list.append(task)

def list_task(tasks_list):
    if not tasks_list:
        print("Doesn't exist task yet!\nPlease add task!")
    else:
        print("All tasks:")
        count = 0
        for task in tasks_list:
            count +=1
            print(f"Task #{count}:")
            for key, value in task.items():
                print(f"\t{key}: {value}")
            print("\n")
def mark_as_done(tasks_list):
    if not tasks_list:
        print("Doesn't exist task yet!\nPlease add task!")
    else:
        ...

def delete_task(tasks_list):
    if not tasks_list:
        print("Doesn't exist task yet!\nPlease add task!")
    else:
        name = int(input("Enter the task ID to delete: "))
        found = False
        for task in tasks_list:
            if name==task["ID"]:
                tasks_list.remove(task)
                print("Mission completed!")
                found =True
                break
    if not found:
        print("You don't have such kind task!")

def filter_by_tag(tasks_list):
    if not tasks_list:
        print("Doesn't exist task yet!\nPlease add task!")
    else:
        ...

def statistics_of_tasks(tasks_list):
    if not tasks_list:
        print("Doesn't exist task yet!\nPlease add task!")
    else:
        ...

def exit(tasks_list):
    print("\nProgram finished!")

tasks_list = []

print("Choose to update your to-do list: ")
print("\t1. Add task")
print("\t2. List task")
print("\t3. Mark as done")
print("\t4. Delete task")
print("\t5. Filter by tag")
print("\t6. Statistics")
print("\t0. Exit")


while True:
    choice = input("\nYour choise: ")
    if not choice.isdigit():
        print("Enter a number!")
        continue
    else:
        choice = int(choice)
    if (choice<0 or choice>6):
        print("Please enter number 1-6!\nEnter 0 to exit!")
        continue
    if choice==1:
        add_task(tasks_list)
    elif choice==2:
        list_task(tasks_list)
    elif choice==3:
        mark_as_done(tasks_list)
    elif choice==4:
        delete_task(tasks_list)
    elif choice==5:
        filter_by_tag(tasks_list)
    elif choice==6:
        statistics_of_tasks(tasks_list)
    else:
        exit(tasks_list)
        break