from datetime import datetime, timedelta
from Tasks import Task


class UrgentTask(Task):
    def __init__(self, name, description, date_of_creation, status, deadline):
        super().__init__(name, description, date_of_creation, status)
        self.deadline = deadline

    def get(self):
        super().get()
        self.deadline = input("Enter Deadline of the Task: ")

    def display(self):
        super().display()
        print(f"Deadline: {self.deadline}")

    def calculate_remaining_time(self):
        deadline_date = datetime.strptime(self.deadline, "%d %B %Y")
        remaining_time = deadline_date - datetime.now()
        return remaining_time
    