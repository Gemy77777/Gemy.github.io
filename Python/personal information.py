fName = input("what's your name ")
mName = input("what's your middle name ")
lName = input("what's your last name ")
age = int(input("what's your age "))

fName = fName.strip().title()
mName = mName.strip().title()
lName = lName.strip().title()
age = int(age)

print(f"Hello {fName} {mName:.1s} {lName}, you are {age} years old.")