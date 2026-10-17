from datetime import date


def get_user_event():
    #event_name input
    while True:
        back_text()
        event_name = input("Enter the name of the event: ").strip()
        if not any(char.isalpha() for char in event_name):
            print("Event name must include a letter! \n")
            continue
        elif event_name == "back".lower():
            return

        #event_day input
        while True:
            back_text()
            event_day = input("Enter the event day (1-31): ")
            if event_day == "back".lower():
                break
            else:
                try:
                    event_day = int(event_day)
                    if event_day < 1 or event_day > 31:
                        print("Invalid date. Please try again. \n")
                        continue
                except ValueError:
                    print("\nHmm, that date doesn't look right. Please enter a number !\n")
                    continue

            #event_month input
            while True:
                back_text()
                event_month = input("Enter the event month (1-12): ")
                if event_month == "back".lower():
                    break
                else:
                    try:
                        event_month = int(event_month)
                        if event_month < 1 or event_month > 12:
                            print("Invalid date. Please try again. \n")
                            continue
                    except ValueError:
                        print("\nHmm, that date doesn't look right. Please enter a number! \n")
                        continue

                #event_year input
                while True:
                    back_text()
                    event_year = input("Enter the event year (20YY): ")
                    if event_year == "back".lower():
                        break
                    else:
                        try:
                            event_year = int(event_year)
                            if date(event_year, event_month, event_day) <= date.today():
                                print("You can't make an event in the past.")
                                continue
                        except ValueError:
                            print("\nHmm, that date doesn't look right. Please enter a number or a correct [DD/MM/YYYY] \n")
                            continue
                    return {"name": event_name, "date": date(event_year, event_month, event_day)}

def sort_events(events):
    return sorted(events, key=lambda e: e["date"])  # nearest -> farthest

def input_event():
    events.append(get_user_event())

def show_events():
    print("List of events: \n")
    for number, e in enumerate(sort_events(events), start=1):
        print(f"{number}. {e['name']} on {e['date'].strftime('%B %d, %Y')}")

def back_text():
    print('Enter "back" to go back')


    #2 already made events
events = [
    {"name": "Birthday", "date": date(2026, 10, 15)},
    {"name": "Concert", "date": date(2026, 12, 25)},
]








#list of schedule (with 2 examples)
schedule = {
    "Monday": [{'name': 'Thai in Changing World', 'start': '08:30', 'end': '11:30'}],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [{'name': 'Programming', 'start': '12:30', 'end': '16:30'}],
    "Friday": [],
    "Saturday": [],
    "Sunday": []
}

def add_schedule(day, name, time_start_str, time_end_str):

    #if input isn't like Monday, Tuesday, etc. -> return
    if day not in schedule:
        print("Error: Invalid day.")
        return

    #if the inputs are wrong -> return
    try:
        time_start = datetime.strptime(time_start_str, "%H:%M").time()  #(<class 'datetime.time'>)
        time_end = datetime.strptime(time_end_str, "%H:%M").time()
    except ValueError:
        print(f"\n Error: Invalid time format. Please use HH:MM (ex. 08:30).")
        return
    if time_start >= time_end:
        print(f"\n Error: End time ({time_end_str}) must be after start time ({time_start_str}).")
        return


    #save existing variable to compare later
    for event in schedule[day]:
        exist_start = event["start"]    #gives str (<class 'str'>)
        exist_end = event["end"]

        exist_start = datetime.strptime(exist_start, "%H:%M").time()    #converts to time -> (<class 'datetime.time'>)
        exist_end = datetime.strptime(exist_end, "%H:%M").time()

        #return if they overlap
        if time_start < exist_end and time_end > exist_start:
            print(f'Your time ({time_start}-{time_end}) is already taken.')
            return

    #if all good -> save
    schedule[day].append({
        'name': name,
        'start': time_start_str,
        'end': time_end_str
    })
    print(f"\n Success: Scheduled '{name}' on {day} from {time_start_str} to {time_end_str}.")

def delete_schedule(day):

    #if input isn't like Monday, Tuesday, etc. -> return
    if day not in schedule:
        print("Error: Invalid day.")
        return

    #return if schedule is empty
    if not schedule[day]:
        print(f'{day} schedule is empty.')
        return

    #enumerate the list
    for i, event in enumerate(schedule[day]):
        print(f"{i}. {event['name']} on {event['start']}")

def show_schedule():
    for day, sched in schedule.items():
        if sched:
            event_text = ", ".join(f'[{event["name"]}] on ({event["start"]}-{event["end"]})' for event in sched)
        else:
            event_text = "no events scheduled."

        print(f"Schedule for {day}: {event_text}.")




print('Please select a number option:')
print('1. Events')
print('2. Schedule')
user_input = input('')
if user_input == "1":
    while True:
        print('\n Please select a number option:')
        print('1. Show events')
        print('2. Add event')
        print('3. Delete event')
        user_input = input('')
        if user_input == "1":
            show_events()
        elif user_input == "2":
            input_event()

elif user_input == "2":
    print('Please select a number option:')
    print('1. Show schedule')
    print('2. Add schedule')
    print('3. Delete schedule')
    user_input = input('')
    if user_input == "1":
        show_schedule()
