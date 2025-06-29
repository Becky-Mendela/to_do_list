from storage import read_tasks, write_tasks

TASKS_FILE_PATH= "tasks.json"

tasks = read_tasks(TASKS_FILE_PATH)
def show_menu():
    print(".....To_Do_List....")
    print("'1'. Add Task")
    print("'2'. View Task")
    print("'3'. Mark Task as Done")
    print("'4'. Completed tasks")
    print("'5'. Delete Task")
    print("'6'. Exit")
    
def add_task():
    task = input("Enter a task to be done: ")
 
    if any(t['task'] == task for t in tasks):
        print(f"You have already added {task} to the list")
    else:
        tasks.append({'task':task, 'done':False})
        print(f"Task {task} added.")
    
def view_task():
    if not tasks:
        print("No task added yet.")
        return
    print("Your Tasks...")
    for index, task in enumerate(tasks, start=1):
        status = 'completed' if task['done'] else "not completed"
        print(f"{index}: {task['task']} [{status}]")

def mark_task():
    view_task()
    if not tasks:
        return
    try:
        index = int(input("Enter the number of task to be marked: "))-1
        if 0 <= index < len(tasks):
            tasks[index]['done'] = not tasks[index]['done']
            status = 'done' if tasks[index]['done'] else 'not done'
            print(f"Marked as {status}.")
            # tasks[index]['done'] = True
            # print("Marked as done.")
        else:
            print("Invalid input!")
    except ValueError:
        print("Please enter a valid number.")
def number_of_completed_task():
    view_task()
    if not tasks:
        return
    tasks_done = len([t for t in tasks if t['done']])
    print(f"You have completed {tasks_done} tasks")
    
def delete_task():
    view_task()
    if not tasks:
        return
    try:
        index = int(input("Enter a number of a task to delete: "))-1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid input.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Enter an option(1-5): ").strip()
            
        if choice == '1':
            add_task()
        elif choice == '2':
            view_task()
        elif choice == '3':
            mark_task()
        elif choice == '4':
            number_of_completed_task()
        elif choice == '5':
            delete_task()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")
        
if __name__ == "__main__":
    main()