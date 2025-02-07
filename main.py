import json
import textwrap
import pprint

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
        while True:
            # used to return to Home page
            goHome = False
            # Enter the home page
            home_page_statement = '''
            Hello and welcome to the Walla Walla,WA event app!
            Here you can view upcoming events or create your own!
            '''
            print(textwrap.dedent(home_page_statement))
            # help document
            help_input = input('Want to refer to the help document before proceeding? (y/n): ')
            if help_input == 'y':
                with open('help document.txt','r',encoding='utf-8') as help_file:
                    help_document = help_file.read()
                    print(help_document)
            # create an event
            create_event_input = input('Would you like to create an event? (y/n): ')
            if create_event_input == 'y':
                while goHome is False:
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
                    if template_event_response == 'n':              # create custom event
                        chosen_event = input('What type of event will this be?: ')
                    # enter event details
                    event_date = input('When will the event be? (enter date): ')
                    print('Please add a description:')
                    event_description = input()
                    # create event object
                    eventObj = {'name': chosen_event,
                                'date': event_date,
                                'description': event_description

                    }
                    print('Are you sure you want to create this event?')
                    print('Event: ',chosen_event)
                    print('Date: ',event_date)
                    print('Description: ',event_description)
                    confirm_create = input('Confirm (y/n): ')
                    if confirm_create == 'y':
                        # add created event to event log
                        with open('events.txt','r',encoding='utf-8') as eventFile:
                            eventData = json.load(eventFile)
                            eventData[chosen_event] = eventObj      # event name is key
                        with open('events.txt','w',encoding='utf-8') as eventFile:
                            json.dump(eventData,eventFile,indent=4)
                    # ask to return to home page
                    returnHome = input('Return to Home Page? (y/n): ')
                    if returnHome == 'y':
                        goHome = True
            # asking user if they want to view events
            if goHome is False:
                view_event_input = input('Would you like to view upcoming events? (y/n): ')
                if view_event_input == 'y':
                    while goHome is False:
                        # enter the view events page
                        view_event_statement = '''
                        Welcome to the events viewing page.
                        '''
                        print(textwrap.dedent(view_event_statement))
                        view_little = input('Would you like to only see the name and date of the events? (y/n): ')
                        if view_little == 'n':
                            view_big = input('Would you like to see all information regarding the events? (y/n): ')
                            if view_big == 'y':
                                with open('events.txt', 'r', encoding='utf-8') as eventFile:
                                    eventData = json.load(eventFile)
                                print()
                                for eventName in eventData:                 # print out events
                                    eventDict = eventData[eventName]
                                    print('Event: ', eventDict['name'])
                                    print('Date:', eventDict['date'])
                                    print('Description: ', eventDict['description'])
                                    print()

                        elif view_little == 'y':
                            with open('events.txt', 'r', encoding='utf-8') as eventFile:
                                eventData = json.load(eventFile)
                            print()
                            for eventName in eventData:             # print out only name and date
                                eventDict = eventData[eventName]
                                print('Event: ', eventDict['name'])
                                print('Date:', eventDict['date'])
                                print()
                        # ask to return to home page
                        returnHome = input('Return to Home Page? (y/n): ')
                        if returnHome == 'y':
                            goHome = True


















