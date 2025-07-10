if __name__ == "__main__":
    tasks = []
    print("Welcome to the TO DO LIST App")
    while True:
        print("\n")
        print("Select one of the following options : ")
        print("1. Enter a task")
        print("2. Delete a task")
        print("3. List all the tasks")
        print("4. Exit")

        choice = int(input("Enter your choice : "))
    
        match choice:
            case 1:
                task = input("Enter your new task : ")
                tasks.append(task)
                print(f"Task '{task}' has been added.")

            case 2:
                task = input("Enter the task you want to delete : ")
                if task in tasks:
                    tasks.remove(task)
                    print(f"Task '{task}' has been deleted.")
                else:
                    print(f"Task '{task}' is not found.")

            case 3:
                if not tasks:
                    print("The list is empty.")
                else:
                    for x in tasks:
                        print(x)

            case 4:
                break
        
            case _:
                print("Invalid input. Please try again later.")

    print("Goodbye!!")

