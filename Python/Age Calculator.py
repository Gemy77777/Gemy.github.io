while True:
    from datetime import datetime
    continue_or_not = input("press Enter to continue or e to exit: ")
    if continue_or_not == "e":
        print('ok.. bye bye<3')
        break
    else:
        pass
    try:
        # Ask user for their birth date
        birth_str = input("Please enter your birth date (YYYY-MM-DD): ").strip()
        birth_date = datetime.strptime(birth_str, "%Y-%m-%d")  # Convert input to datetime object

        # Get current date and time
        now = datetime.now()

        # Calculate the difference between now and birth date
        delta = now - birth_date

        if delta.days < 0:
            print("Invalid birth date. Date is in the future.")
            continue

        # Calculate age in different units
        years = delta.days // 365
        months = delta.days // 30
        weeks = delta.days // 7
        days = delta.days
        minutes = int(delta.total_seconds() // 60)
        seconds = int(delta.total_seconds())

        # Ask user for the unit to display
        unit = input("Please enter the unit (years/months/weeks/days/minutes/seconds): ").strip().lower()

        if unit == "years" or unit == "y":
            print(f"You are approximately {years} years old.")
        elif unit == "months" or unit == "m":
            print(f"You are approximately {months} months old.")
        elif unit == "weeks" or unit == "w":
            print(f"You are approximately {weeks} weeks old.")
        elif unit == "days" or unit == "d":
            print(f"You are approximately {days} days old.")
        elif unit == "minutes" or unit == "min":
            print(f"You are approximately {minutes} minutes old.")
        elif unit == "seconds" or unit == "sec":
            print(f"You are approximately {seconds} seconds old.")
        else:
            print("Invalid unit.")
    except ValueError:
        print("Invalid input. Please enter the date in YYYY-MM-DD format and valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")