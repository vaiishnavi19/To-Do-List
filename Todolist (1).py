import os 

def show_tasks(tasks):
    if not tasks:
        print("no tasks found.")
    else:
        for i, task in enumerate(tasks,1):
            print(f"{i}.{task}") 
def add_task(tasks, new_tasks): 
    tasks.append(new_tasks)
    print("task added succussfully.")
    def update_task(tasks, index, updated_task):
        if 1 <= index <=len(tasks): 
            print("task updated succussfully.")
        else:
            print("invalid task index.")
def delet_task(tasks, index):
    if 1 <= index <=len(tasks):
         delete_tasks = tasks.pop(index-1 )
         print(f"task'{delet_task}' deleted succussfully.")
    else:
         print("invalid task index.")
def save_task_to_file(file_path, tasks): 
    with open(file_path, "w") as file:
        for task in tasks:
            file.write(f"{task}\n") 
def load_tasks_from_file(file_path):
    task = [] 
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            task=file.read().splitlines()
        return task



def main(): 
    file_path = "todo_list.txt"
    tasks = load_tasks_from_file(file_path)
    while True:
        print("\n===== to.do list=====")
        print("1.show tasks")
        print("2.add tasks")
        print("3.update tasks")
        print("4.delete tasks")
        print("5.save and exit")
        choice = input("entre your chioce(1-5); ") 
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2": 
            new_task = input("enter task to add:")
            add_task(tasks, new_task)
        elif choice == "3": 
            index = int(input("enter the task index to update: "))
            update_task = input("enter the updated task: ")
            update_task(tasks,index, update_task)
        elif choice =="4": 
            index = int(input("enter the task intex to delet: "))
            delet_task(tasks, index) 
        elif choice == "5":
            save_task_to_file(file_path, tasks)
            print("task saved. Exiting..")
            break
        else:
            print("invalid choice. pls try again") 

if __name__ == "__main__":
    main()


