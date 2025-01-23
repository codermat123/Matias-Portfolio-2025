import json

def load_tasks():
    try:
        #Open & Read tasks from tasks.json
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError: #If no file, return empty list
        return []

def save_tasks(tasks):
    #Save tasks to tasks.json
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def main():
    tasks = load_tasks()

    while True:
        print("\n===== 📲To-Do List =====")
        print("1. 📥Add Task")
        print("2. 📊Show Tasks")
        print("3. ✅Mark Task as Done")
        print("4. 🔴Exit (Please Exit before leaving)")

        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            n_tasks = int(input("How many tasks do you want to add: "))
            
            #Loop to gather & add tasks
            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False}) #Add new undone task to list
                print("Task added!")

        elif choice == '2':
            #Display tasks + status 
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}") 

        elif choice == '3':
            #Allow user to mark task done 
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks): #ensure value within index range
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")

        elif choice == '4':
            #Save task to file before exiting
            print("Exiting the To-Do List.")
            save_tasks(tasks)
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
