class Task():
    def __init__(self, name, description, date_of_creation, status):
        self.name = name
        self.description = description
        self.dateOfCreation = date_of_creation
        self.status = status

    def display(self):
        print(f"Title of Task: {self.name}")
        print(f"Description of Task: {self.description}")
        print(f"Date of Creation: {self.dateOfCreation}")
        print(f"Status of Task: {self.status}")

    def get(self):
        print("----------------------------------")
        self.name = input("Enter Title: ")
        self.description = input("Enter Description: ")
        self.dateOfCreation = input("Enter Date of Creation: ")
        self.status = input("Enter Status: ").upper()

    def mark_as_completed(self):
        """
        Marks the task as completed, if the task is already completed this method will return True
        and print a statement that will print 'Task already completed.'
        """
        if self.status != "completed":
            self.status = "completed"
            print("Hurray! The task is now completed.")
            return True
        else:
            print("Task is already completed")
            return True
