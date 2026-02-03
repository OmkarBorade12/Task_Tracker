def main():
    tasks = []
    
    while True:
        print("\n--- Task Tracker Menu ---")
        print("Commands: add, view, complete, exit")
        
        command = input("Enter command: ").strip().lower()
        
        if command == 'add':
            task = input("Enter task description: ").strip()
            if task:
                tasks.append(task)
                print(f"Task added: {task}")
            else:
                print("Task description cannot be empty.")
        
        elif command == 'view':
            print("\nCurrent Tasks:")
            if not tasks:
                print("No tasks found.")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
        
        elif command == 'complete':
            if not tasks:
                print("No tasks to complete.")
                continue
                
            
            print("\nSelect a task to complete:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
                
            task_num_input = input("Enter task number to complete: ").strip()
            
            if not task_num_input.isdigit():
                print("Please enter a valid number.")
                continue
                
            task_index = int(task_num_input) - 1
            
            if 0 <= task_index < len(tasks):
                current_task = tasks[task_index]
                if current_task.startswith("[x] "):
                    print("Task is already completed.")
                else:
                    tasks[task_index] = "[x] " + current_task
                    print(f"Task marked as completed: {tasks[task_index]}")
            else:
                print("Invalid task number.")
        
        elif command == 'exit':
            print("Goodbye!")
            break
            
        else:
            print("Unknown command. Please try 'add', 'view', 'complete', or 'exit'.")

if __name__ == "__main__":
    main()
