from Tasks import Task


class RoutineTask(Task):
    def __init__(self, name, description, date_of_creation, status, frequency):
        super().__init__(name, description, date_of_creation, status)
        self.frequency = frequency

    def get(self):
        super().get()
        self.frequency = input("Enter Frequency of the Task: ")

    def display(self):
        super().display()
        print(f"Task is done {self.frequency} times in a week")

    def calculate_days_per_week(self):
        return self.frequency
    