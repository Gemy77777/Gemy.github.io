tries = 3
password = "Kira@123"
user = input("Enter your username: ")
while tries > 0:
    password = input("Enter your password: ")
    if password == "Kira@123":
        print("Access granted.")
        print(f"Welcome, {user.title()}!")
        break
    else:
        tries -= 1
        print(f"Incorrect password. You have {'The last' if tries == 1 else tries} {'chance' if tries == 1 else 'chances'} {'left' if tries > 0 else 'out of attempts'}")