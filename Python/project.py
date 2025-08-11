fName = input("Enter your first name: ")
mName = input("Enter your middle name: ")
lName = input("Enter your last name: ")
age = int(input("Enter your age: "))

fName = fName.strip().title()
mName = mName.strip().title()
lName = lName.strip().title()
age = int(age)

print(f"Hello {fName} {mName:.1s} {lName}, you are {age} years old.")