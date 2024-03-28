from UrgentTask import UrgentTask
from LocationBasedTask import LocationBasedTask
from RoutineTask import RoutineTask


class List:
    def __init__(self):
        self.tasks = []

    def add_tasks(self):
        quantity = int(input("How many tasks you want to add? "))
        for i in range(quantity):
            task_type = int(input("\n1. Routine Tasks - Tasks to be done frequently 🤠"
                                  "\n2. Urgent Tasks - Tasks with a deadline 🤯 "
                                  "\n3. Location Based Tasks - Tasks associated with a location 🏢"
                                  "\nTo which category do you want to add? "))
            if task_type == 1:
                task_to_add = RoutineTask(None, None, None, None, None)
                task_to_add.get()
                self.tasks.append(task_to_add)
            elif task_type == 2:
                task_to_add = UrgentTask(None, None, None, None, None)
                task_to_add.get()
                self.tasks.append(task_to_add)
            elif task_type == 3:
                task_to_add = LocationBasedTask(None, None, None, None, None)
                task_to_add.get()
                self.tasks.append(task_to_add)
            else:
                print("Invalid Entry, Please try again 🙁")

    def view_categories(self):
        total_tasks = len(self.tasks)
        r_tasks = sum(isinstance(Task, RoutineTask) for Task in self.tasks)
        u_tasks = sum(isinstance(Task, UrgentTask) for Task in self.tasks)
        l_tasks = sum(isinstance(Task, LocationBasedTask) for Task in self.tasks)
        print(f"\nThere are total {total_tasks} Tasks are categorized as follows:"
              f"\nRoutine Tasks - Tasks to be done frequently 🤠 ; They are {r_tasks}"
              f"\nUrgent Tasks - Tasks with a deadline 🤯 ; They are {u_tasks}"
              f"\nLocation Based Tasks - Tasks associated with a location 🏢 ; They are {l_tasks}")

    def view_all_tasks(self):
        print("All Tasks are as follows: ")
        i = 0
        for task in self.tasks:
            i += 1
            print(f"     -------- Task # {i} ---------\n")
            print(task.display())

    def view_urgent_tasks(self):
        print("Urgent Tasks are as follows: \n")
        i = 0
        for task in self.tasks:
            i += 1
            if isinstance(task, UrgentTask):
                print(f"     -------- Task # {i} ---------\n")
                print(task.display())

    def view_routine_tasks(self):
        print("Routine Tasks are as follows: \n")
        i = 0
        for task in self.tasks:
            if isinstance(task, RoutineTask):
                i += 1
                print(f"     -------- Task # {i} ---------\n")
                print(task.display())

    def view_location_tasks(self):
        print("Location based Tasks are as follows: \n")
        i = 0
        for task in self.tasks:
            i += 1
            if isinstance(task, LocationBasedTask):
                print(f"     -------- Task # {i} ---------\n")
                print(task.display())

    def view_completed_tasks(self):
        i = 0
        print("Completed Tasks are as follows: \n")
        i += 1
        for task in self.tasks:
            print(f"     -------- Task # {i} ---------\n")
            if task.status == "COMPLETED":
                print(task)

    def view_pending_tasks(self):
        pass

    def update_task_status(self):
        task_to_update = input("Enter index of the task you want to update: ")
        pass

    def reschedule_urgent_tasks(self):
        pass

    def calculate_frequent_task(self):
        pass

    def search_tasks(self):
        pass

    def calculate_remaining_time(self):
        pass

    def delete_tasks(self):
        pass
