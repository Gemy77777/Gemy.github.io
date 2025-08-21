#salary type
customers = {
    'Gemy': 110000,
    "John": 45000,
    "Jane": 60000,
    "Doe": 120000,
    "Smith": 80000
}
def check_salary(salary):
    if salary < 50000:
        return "Low"
    elif 50000 <= salary < 100000:
        return "Medium"
    else:
        return "High"
MySalaries = [salary for salary in customers.values()]
mySalaryResult = map(check_salary, MySalaries)
for name, salary in zip(customers.keys(), mySalaryResult):
    print(f'- {name.capitalize().title()}: {salary}')
