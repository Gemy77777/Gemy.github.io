from datetime import datetime, timedelta

while True:
    continue_or_not = input("Press Enter to continue or e to exit: ")
    if continue_or_not == "e":
        print('ok.. bye bye<3')
        break
    try:
        birth_str = input("Please enter your birth date (YYYY-MM-DD): ").strip()
        birth_date = datetime.strptime(birth_str, "%Y-%m-%d")
        now = datetime.now()
        if birth_date > now:
            print("Invalid birth date. Date is in the future.")
            continue

        years = now.year - birth_date.year
        months = now.month - birth_date.month
        days = now.day - birth_date.day

        if days < 0:
            months -= 1
            previous_month = now.month - 1 or 12
            previous_year = now.year if now.month != 1 else now.year - 1
            last_day_of_previous_month = (datetime(previous_year, previous_month % 12 + 1, 1) - timedelta(days=1)).day
            days += last_day_of_previous_month

        if months < 0:
            years -= 1
            months += 12

        print(f"You have lived for {years} years, {months} months and {days} days.")
    except ValueError:
        print("Invalid input. Please enter the date in YYYY-MM-DD format and valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")