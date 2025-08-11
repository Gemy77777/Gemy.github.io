import datetime
birthYear = int(input("Enter your birth date: "))
age = datetime.datetime.now().year - birthYear
print('Your age is ', age, 'years old')