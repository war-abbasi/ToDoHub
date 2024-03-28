from Tasks import Task


class LocationBasedTask(Task):
    def __init__(self, name, description, date_of_creation, status, location):
        super().__init__(name, description, date_of_creation, status)
        self.location = location

    def get(self):
        super().get()
        self.location = input("Enter Location for the Task: ")

    def display(self):
        super().display()
        print(f"Location: {self.location}")
        