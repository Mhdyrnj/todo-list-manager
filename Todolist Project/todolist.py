import csv
import os
PRIORITY_ORDER = {"High": 1, "Medium": 2, "Low": 3}
class Task:
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority

    def __str__(self):
        return f"[{self.priority}] {self.name} - {self.description}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added.")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"Task '{removed.name}' removed.")
        else:
            print("Invalid task number.")

    def show_tasks(self):
        if not self.tasks:
            print("The to-do list is empty.")
            return
        self.tasks.sort(key=lambda task: PRIORITY_ORDER[task.priority])
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")


    def save_to_csv(self, filename="tasks.csv"):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "description", "priority"])
            for task in self.tasks:
                writer.writerow([task.name, task.description, task.priority])
        print("Tasks saved.")

    def load_from_csv(self, filename="tasks.csv"):
        if not os.path.exists(filename):
            print("No saved file found. Starting with an empty list.")
            return
        self.tasks = []
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                priority = row["priority"].strip().capitalize()
                if priority not in PRIORITY_ORDER:
                    priority = "Medium"
                self.tasks.append(Task(row["name"], row["description"], priority))
        print("Tasks loaded.")
        
def show_menu():
    print("\n===== To-Do List =====")
    print("1. Add task")
    print("2. Remove task")
    print("3. Show tasks")
    print("4. Save tasks")
    print("5. Exit")


def get_priority():
    options = {"1": "High", "2": "Medium", "3": "Low"}
    while True:
        choice = input("Priority (1=High, 2=Medium, 3=Low): ")
        if choice in options:
            return options[choice]
        print("Invalid choice. Please enter 1, 2, or 3.")

def get_name():
    while True:
        name = input("Task name: ").strip()
        if name:
            return name
        print("Name cannot be empty.")


def main():
    todo = ToDoList()
    todo.load_from_csv()
    

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            name = get_name()
            description = input("Description: ")
            priority = get_priority()
            todo.add_task(Task(name, description, priority))

        elif choice == "2":
            todo.show_tasks()
            try:
                number = int(input("Task number to remove: "))
                todo.remove_task(number - 1)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            todo.show_tasks()

        elif choice == "4":
            todo.save_to_csv()

        elif choice == "5":
            todo.save_to_csv()
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


main()
