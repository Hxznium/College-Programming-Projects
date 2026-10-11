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
                            if date(event_year, event_month, event_day) < date.today():
                                print("You can't make an event in the past.")
                                continue
                        except ValueError:
                            print("\nHmm, that date doesn't look right. Please enter a number or a correct [DD/MM/YYYY] \n")
                            continue
                    return {"name": event_name, "date": date(event_year, event_month, event_day)}

def sort_events(events):
    return sorted(events, key=lambda e: e["date"])  # nearest -> farthest

def input_event():
    #1 event from the user
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




whole_week = [sunday, monday, tuesday, wednesday, thursday, friday, saturday]






show_events()
input_event()
