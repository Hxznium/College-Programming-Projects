from datetime import date

def get_user_event():
    #event_name input
    while True:
        event_name = input("Enter the name of the event: ").strip()
        if not any(char.isalpha() for char in event_name):
            print("Event name must include a letter!\n")
            continue
        elif event_name == "back".lower():
            return

        #event_date input
        while True:
            try:
                event_date = int(input("Enter the event day (1-31): "))
                if event_date < 1 or event_date > 31:
                    print("Invalid date. Please try again.\n")
                    continue
            except ValueError:
                print("\nHmm, that date doesn't look right. Please enter a number!\n")

            #event_month input
            while True:
                try:
                    event_month = int(input("Enter the event month (1-12): "))
                    if event_month < 1 or event_month > 12:
                        print("Invalid date. Please try again.\n")
                        continue
                except ValueError:
                    print("\nHmm, that date doesn't look right. Please enter a number!\n")

                #event_year input
                while True:
                    try:
                        event_year = int(input("Enter the event year (20YY): "))
                        if date
                        break
                    except ValueError:
                        print("\nHmm, that date doesn't look right. Please enter a number!\n")
    return {"name": event_name, "date": date(event_year, event_month, event_date)}

def sort_events(events):
    return sorted(events, key=lambda e: e["date"])  # nearest -> farthest

def main():
    print("Hi there! I already have 2 events saved for you.")
    print("Add one more, and I'll put them all in order.\n")

    # 2 already made events
    events = [
        {"name": "Birthday", "date": date(2026, 10, 15)},
        {"name": "Concert", "date": date(2026, 12, 25)},
    ]

    # 1 event from the user
    events.append(get_user_event())

    print("\nAll done! Here's what's coming up, from soonest to furthest away:\n")
    for number, e in enumerate(sort_events(events), start=1):
        print(f"{number}. {e['name']} on {e['date'].strftime('%B %d, %Y')}")

    print("\nHave fun at your events!")

main()
