task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Try to complete it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that is time-sensitive. Plan your day accordingly.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Address it when you can.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task but still time-sensitive.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Reminder: Unrecognized priority level.")
