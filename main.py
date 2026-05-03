# Smart Task Automation - CLI Task Manager

import sys

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task = input("Enter task: ").strip()
        if task:
            self.tasks.append(task)
            print(f"✅ Task '{task}' added!")
        else:
            print("⚠️ Task cannot be empty.")

    def view_tasks(self):
        if not self.tasks:
            print("📭 No tasks available.")
            return

        print("\n📌 Your Tasks:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def run(self):
        while True:
            print("\n--- Task Manager ---")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_task()

            elif choice == "2":
                self.view_tasks()

            elif choice == "3":
                print("👋 Exiting... Goodbye!")
                sys.exit()

            else:
                print("❌ Invalid choice, try again.")


if __name__ == "__main__":
    app = TaskManager()
    app.run()