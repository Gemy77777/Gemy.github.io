while True:
    print('Hello!')
    input('Welcome to the admin panel. Press Enter to continue...')
    Admins = ['Gamal', 'Ahmed', 'Sara', 'John', 'Osama']
    UserName = input('Please enter your username:').strip().capitalize()

    if UserName in Admins:
        print(f'Welcome {UserName}!')
        print('Thank you for your interest.')
        if input('Press e to exit the program or c to continue: ').strip().lower() == 'e':
            break
        else:
            continue           
    else:
        print('Access denied.')
        if input('Do you want to join the admin team? (Y/N) ').strip().upper() == 'Y':
            NewAdmin = input('Please enter your name:').strip().capitalize()
            Admins.append(NewAdmin)
            print(f'Congratulations {NewAdmin}, you have been added to the admin team!')
            print('Admins:', Admins)
        else:
            print('Thank you for your interest.')
            input('Press e to exit the program.')
            if input().strip().lower() == 'e':
                break
