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
        # Enter the home page
        home_page_statement = '''
        Hello and welcome to the Walla Walla,WA event app!
        Here you can view upcoming events or create your own!
        '''
        print(textwrap.dedent(home_page_statement))
        view_event_input = input('Would you like to view upcoming events? (y/n): ')
        create_event_input = input('Would you like to create an event? (y/n): ')
        if create_event_input == 'y':
            # Enter the Event Creation Page
            event_statement = '''
            Hello and Welcome to the event creation page. 
            Here you can create events and add them to our logs. Other users
            will then be able to view/attend your event!
            '''
            print(textwrap.dedent(event_statement))
            template_event_response = input('Would you like to use an event from our list? (y/n): ')
            if template_event_response == 'y':     # use template event
                template_event_list = '''
                Which event would you like? (choose number)
                1. Concert
                2. Eating Contest
                3. Movie in the Park
                '''
                print(textwrap.dedent(template_event_list))
                template_events = { 1: 'Concert',
                                    2: 'Eating Contest',
                                    3: 'Movie in the Park'

                                    }
                event_input = int(input())
                chosen_event = template_events[event_input]
                print('You chose to create this event: ', chosen_event)
            else:
                chosen_event = input('What type of event will this be?: ')
                event_date = input('When will the event be? (enter date): ')
                print('Please add a description:')
                event_description = input()








