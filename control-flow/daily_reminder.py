task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f'"{task}" is a high priority task that requires immediate attention today!')
        else:
            print(f'"{task}" is high priority. Try to get it done soon.')
    case "medium":
        if time_bound == "yes":
            print(f'"{task}" is medium priority and time-bound. Plan accordingly.')
        else:
            print(f'"{task}" is medium priority. Get to it when possible.')
    case "low":
        if time_bound == "yes":
            print(f'"{task}" is low priority but still time-sensitive. Don’t forget it!')
        else:
            print(f'"{task}" is a low priority task. Consider completing it when you have free time.')
    case _:
        print("Unknown priority level entered.")
