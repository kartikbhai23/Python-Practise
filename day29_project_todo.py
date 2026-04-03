# Day 29: Todo Manager CLI
# task logger CLI saving text lines to a file

import os

class TodoList:
    def __init__(self, filename="todo_list.txt"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]

    def save_tasks(self):
        with open(self.filename, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task added: '{task}'")

    def show_tasks(self):
        if not self.tasks:
            print("List is empty.")
        else:
            print("\nPending Tasks:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

    def remove_task(self, index):
        try:
            removed = self.tasks.pop(index - 1)
            self.save_tasks()
            print(f"Task deleted: '{removed}'")
        except IndexError:
            print("Index range error!")

def run_todo_app(mock_inputs=None):
    todo = TodoList("temp_todo.txt")
    input_idx = 0
    
    def get_input(prompt):
        nonlocal input_idx
        if mock_inputs is not None:
            if input_idx < len(mock_inputs):
                val = mock_inputs[input_idx]
                input_idx += 1
                print(f"{prompt}{val}")
                return val
            return "4"
        return input(prompt)

    while True:
        print("\n--- Todo App ---")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = get_input("Choice: ")
        if choice == "1":
            task_name = get_input("Task name: ")
            todo.add_task(task_name)
        elif choice == "2":
            todo.show_tasks()
        elif choice == "3":
            todo.show_tasks()
            try:
                num = int(get_input("Task number: "))
                todo.remove_task(num)
            except ValueError:
                print("Use numerical values!")
        elif choice == "4":
            print("Exit todo app.")
            break
        else:
            print("Bad options!")

    if os.path.exists("temp_todo.txt"):
        os.remove("temp_todo.txt")

if __name__ == "__main__":
    run_todo_app(mock_inputs=["1", "Study numpy", "1", "Build Project", "2", "3", "1", "4"])
