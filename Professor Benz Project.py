from datetime import date

def get_user_event():
    #event_name input
    while True:
        back_text()
        event_name = input("Enter the name of the event: ").strip()
        if not any(char.isalpha() for char in event_name):
            print("Event name must include a letter!")
            continue
        elif event_name == "back".lower():
            return False

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
                        print("Invalid date. Please try again.")
                        continue
                except ValueError:
                    print("Hmm, that date doesn't look right. Please enter a number !")
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
                            print("Invalid date. Please try again.")
                            continue
                    except ValueError:
                        print("Hmm, that date doesn't look right. Please enter a number!")
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
                            if date(event_year, event_month, event_day) < date.today():
                                print("You can't make an event in the past.")
                                continue
                        except ValueError:
                            print("Hmm, that date doesn't look right. Please enter a number or a correct [DD/MM/YYYY]")
                            continue
                    return {"name": event_name, "date": date(event_year, event_month, event_day)}

def sort_events(events):
    return sorted(events, key=lambda e: e["date"])  # nearest -> farthest

def show_events():
    print("List of events: \n")
    for number, e in enumerate((events), start=1):
        print(f"{number}. {e['name']} on {e['date'].strftime('%B %d, %Y')}")

def show_event_today():
    today = date.today()
    today_events = [e for e in events if e["date"] == today]

    print("Today's events:\n")

    for number, e in enumerate(today_events, start=1):
        print(f"{number}. {e['name']} on {e['date'].strftime('%B %d, %Y')}")

    if not today_events:
        print('There is no event today!')

def back_text():
    print('\nEnter "back" to go back')

def delete_event():
    while True:
        for number, e in enumerate(events, start=1):
            print(f"{number}. {e['name']} on {e['date'].strftime('%B %d, %Y')}")

        back_text()
        choice = (input("Enter a number option to delete: "))

        if choice == "back".strip().lower():
            return

        else:
            try:
                choice = int(choice)
            except ValueError:
                print("Invalid option, Please enter a number!")
                continue

        if choice < 1 or choice > len(events):
            print("Invalid number. Try again.")
            continue

        delete_event = events[choice - 1]
        events.remove(delete_event)
        print(f"Event [{delete_event['name']}] is deleted!")
        return
    #2 already made events
events = [
    {"name": "Exam", "date": date(2026, 11, 5)},
    {"name": "Birthday", "date": date(2026, 11, 25)},
    {"name": "Concert", "date": date(2026, 12, 10)},
]
print('This is -- NOWN ---')
print('Welcome to our system program application!')
while True:
    print('\nPlease select a number option:')
    print('1. Show events')
    print('2. Add event')
    print('3. Delete event')
    user_input = input('')
    if user_input == "1":
        while True:
            back_text()
            print('1. Show all events')
            print('2. Show today event')
            user_input = input("Please select a number option: ")
            if user_input == "back".strip().lower():
                break
            elif user_input == "1":
                show_events()
                break
            elif user_input == "2":
                show_event_today()
                break
            else:
                print("Invalid option, Please enter a number!")
                continue
    elif user_input == "2":
        new_event = get_user_event()

        if new_event is not False:
            events.append(new_event)
    elif user_input == "3":
        delete_event()
    else:
        print("Invalid option, Please enter a number!")
