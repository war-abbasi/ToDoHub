from List import List
from UrgentTask import UrgentTask
from LocationBasedTask import LocationBasedTask
from RoutineTask import RoutineTask
from Tasks import Task

# Initialize the task list
task_list = List()

while True:
    print("-------------------------------"
          "\n1. Add/Create tasks"
          "\n2. View Task Categories"
          "\n3. View all Tasks"
          "\n4. View Urgent Tasks only"
          "\n5. View Routine Tasks only"
          "\n6. View Location Based Tasks only"
          "\n7. View Completed Tasks"
          "\n8. View Pending Tasks"
          "\n9. Mark Task as Completed"
          "\n10. Reschedule Urgent Tasks"
          "\n11. Display most frequent Routine Task"
          "\n12. Search Tasks by Title"
          "\n13. Calculate Remaining Time for Urgent Task"
          "\n14. Delete a Task"
          "\n--------------------------------")
    choice = int(input("Select an option to begin 🤩\n"))
    if choice == 1:
        task_list.add_tasks()
    elif choice == 2:
        task_list.view_categories()
    elif choice == 3:
        task_list.view_all_tasks()
    elif choice == 4:
        task_list.view_urgent_tasks()
    elif choice == 5:
        task_list.view_routine_tasks()
    elif choice == 6:
        task_list.view_location_tasks()
    elif choice == 7:
        task_list.view_completed_tasks()
    elif choice == 8:
        task_list.view_pending_tasks()
    elif choice == 9:
        task_list.update_task_status()
    elif choice == 10:
        task_list.reschedule_urgent_tasks()
    elif choice == 11:
        task_list.calculate_frequent_task()
    elif choice == 12:
        task_list.search_tasks()
    elif choice == 13:
        task_list.calculate_remaining_time()
    elif choice == 14:
        task_list.delete_tasks()
    elif choice == 0:
        break
    else:
        print("Invalid choice")
