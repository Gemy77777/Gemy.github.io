username = input("Enter a username: ")
if len(username) < 5:
    print("Username must be at least 5 characters long.")
elif len(username) > 15:
    print("Username must be no more than 15 characters long.")
elif username.find(" ") != -1:
    print("Username must not contain spaces.")
elif username.isalpha() == False:
    print("Username must contain only letters.")
else:
    print(f"Username is valid.")
    print(f"Hello, {username}!")