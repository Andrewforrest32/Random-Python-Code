sched_mon = []
sched_tues = []
sched_wed = []
sched_thurs = []
sched_fri = []
schedule = {
    "Monday":sched_mon,"Tuesday":sched_tues,"Wednesday":sched_wed,
    "Thursday":sched_thurs,"Friday":sched_fri
}
days = list(schedule.keys())

print("Let's make your school schedule!")
while True:
    for x in days:
        print(x)
        print(schedule[x])
    while True:
        day = input("What day is your class (enter 'stop' when done): ")
        if day == 'stop':
            break
        elif day not in days:
                print("Invalid day entered")
        else:
            break
    if day == 'stop':
        break
    course = input(f"What class do you have on {day}: ")
    schedule[day].append(course)
    while True:
        multiple_days = input(f"Is {course} on another day (y/n): ")
        if multiple_days != 'y' and multiple_days != 'n':
            print("Invaid answer")
        elif multiple_days == 'n':
            break
        else:
            while True:
                other_day = input("What other day: ")
                if other_day not in days:
                    print("Invalid day entered")
                else:
                    schedule[other_day].append(course)
                    break