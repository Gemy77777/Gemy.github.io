#salary type
customers = {
    'Gemy': 110000,
    "John": 45000,
    "Jane": 60000,
    "Doe": 120000,
    "Smith": 80000,
}

def check_salary(name, salary):
    if salary < 50000:
        return "Low"
    elif 50000 <= salary < 100000:
        return "Medium"
    return "High"

for name, salary in customers.items():
    result = check_salary(name, salary)
    print(f'- {name.capitalize().title()}: {result}')
