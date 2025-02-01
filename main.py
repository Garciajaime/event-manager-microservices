import json


while True:
    loginVerified = False
    login_input = input('Do you have a login? (y/n): ')
    if login_input == 'y':
        username = input('What is your username?: ')
        password = input('What is your password?: ')
        with open('login.txt','r',encoding='utf-8') as loginFile:
            loginData = json.load(loginFile)
            if username in loginData:
                if loginData[username] == password:
                    loginVerified = True
                else:
                    print('ERROR: Your password was incorrect')
            else:
                print('ERROR: Your username or password was incorrect')
    elif login_input == 'n':
        create_login_input = input('Want to create a login? (y/n): ')
        # create login
        if create_login_input == 'y':
            username = input('Enter a username: ')
            password = input('Enter a password: ')
            passConfirm = None
            while password != passConfirm:
                passConfirm = input('Please confirm your password: ')
            loginCredentials = { username: password,

            }
            with open("login.txt","a", encoding="utf-8") as loginFile:
                json.dump(loginCredentials, loginFile, indent=4)

    if loginVerified is True:
        print()
        print()
        print('Congratulations you are logged in!')
        print()
        print()


