tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet")
    else:
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

while True:
    print("\n1. Add task")
    print("2. Show tasks")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()
        num = int(input("Enter task number: "))
        if 0 < num <= len(tasks):
            tasks.pop(num - 1)

    elif choice == "4":
        break
