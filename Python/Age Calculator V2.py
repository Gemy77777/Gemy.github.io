from datetime import datetime
from dateutil.relativedelta import relativedelta  # pip install python-dateutil

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
        diff = relativedelta(now, birth_date)
        start_of_year = datetime(now.year, 1, 1)
        monthsInYear = relativedelta(now, start_of_year)
        print(f"You have lived for {diff.years} years and {monthsInYear.months} months and {monthsInYear.days} days.")
    except ValueError:
        print("Invalid input. Please enter the date in YYYY-MM-DD format and valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")