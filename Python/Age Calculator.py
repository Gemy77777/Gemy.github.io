from datetime import datetime

day = int(input("Enter your birth day (1-31): "))
month = int(input("Enter your birth month (1-12): "))
year = int(input("Enter your birth year (e.g., 2000): "))

delta = datetime.now() - datetime(year, month, day)
print('You lived for:')
print(f'{delta.days // 365} years.')
print(f'{delta.days // 30} months.')
print(f'{delta.days // 7} weeks.')
print(f'{delta.days:,} days.')
print(f'{int(delta.total_seconds() // 3600):,} hours.')
print(f'{int(delta.total_seconds() // 60):,} minutes.')
print(f'{int(delta.total_seconds()):,} seconds.')