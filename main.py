import json
import textwrap

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
            opening_statement = '''
            *Note: We will not share your login info with third party sites.
            Login info will only be used to verify you as a user. 
            '''
            print(textwrap.dedent(opening_statement))
            username = input('Enter a username: ')
            password = input('Enter a password: ')
            passConfirm = None
            while password != passConfirm:
                passConfirm = input('Please confirm your password: ')
            with open("login.txt","r", encoding="utf-8") as loginFile:
                loginData = json.load(loginFile)
                loginData[username] = password            # add new entry to json object
            with open("login.txt","w", encoding="utf-8") as loginFile:
                json.dump(loginData,loginFile, indent=4)  # update json object in login file
    if loginVerified is True:
        print()
        print()
        print('Congratulations you are logged in!')
        print()
        print()


