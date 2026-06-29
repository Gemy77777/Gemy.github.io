import re
while 1:
    email = input("Enter your email address: ")
    phone = input("Enter your phone number: ")
    isEmailValid = re.match(r"^[A-z0-9.]{6,30}+@gmail\.com$", email)
    isPhoneValid = re.match(r"^\d{4}-?\d{3}-?\d{4}$", phone)
    if isEmailValid and isPhoneValid:
        print("Valid credentials")
        break
    else:
        print("Invalid email or phone number")