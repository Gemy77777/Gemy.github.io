name = input("Enter your name: ").title().strip()
email = input("Enter your email: ").strip()
theUserName = email[:email.index('@')]
domain = email[email.index('@')+1:]

print(f'hello {name}, your email is {email}.')
print(f'Your username is {theUserName} and your domain is {domain}.')