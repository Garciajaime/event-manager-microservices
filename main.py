import json
import textwrap
import pprint
import time

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
                                'description': event_description,
                                'username': username

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
                            # create event number
                            keysList = list(eventData.keys())
                            keysList = [int(num) for num in keysList]
                            maxKey = max(keysList)
                            eventNum = maxKey + 1
                            eventObj['Event Number'] = eventNum
                            eventData[eventNum] = eventObj          # event number is key
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
                                    print('Event Number', eventDict['Event Number'])
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
                # enter the deletion/edit page
                deleteEvent = input('Do you want to delete an event? (y/n): ')
                if deleteEvent == 'y':
                    while goHome is False:
                        openingMessage = '''
                        Hello you have entered the event deletion page.
                        Here you can see all the events you have created and
                        decide if you want to delete any.
                        '''
                        print(textwrap.dedent(openingMessage))
                        print()
                        print()
                        # make a request for a users created events
                        with open('EventDelete.txt','w',encoding='utf-8') as delFile:
                            reqMessage = {
                                "Read": username
                            }
                            json.dump(reqMessage,delFile,indent=4)
                        time.sleep(3)
                        # print out all of a user's created events
                        userEventNums = []
                        with open('EventDelete.txt','r',encoding='utf-8') as file:
                            eventObjs = json.load(file)
                            viewEvents = input('Would you like to view all your events? (y/n): ')
                            if viewEvents == 'y':
                                viewEvents = True
                                print('Below are the events that you have created:')
                            for event in eventObjs:
                                currentNum = int(event)
                                userEventNums.append(currentNum)    # create a list of a user's events
                                currentEvent = eventObjs[event]
                                if viewEvents is True:
                                    print('Event Number: ', currentEvent['Event Number'])
                                    print('Event: ', currentEvent['name'])
                                    print('Date:', currentEvent['date'])
                                    print('Description: ', currentEvent['description'])
                                    print()
                        # Delete event section
                        requestDelete = input('Would you like to delete an Event? (y/n): ')
                        if requestDelete == 'y':
                            deleteNum = input('Please enter the "Event Number" of the event you want to delete: ')
                            deleteNum = int(deleteNum)
                            while deleteNum not in userEventNums:
                                print('ERROR: The Event Number you have entered is invalid.')
                                deleteNum = input('Please enter the "Event Number" of the event you want to delete: ')
                                deleteNum = int(deleteNum)
                            confirmDelete = input(f'Are you sure you want to delete Event Number "{deleteNum}" (y/n)?: ')
                            if confirmDelete == 'y':
                                with open('EventDelete.txt','w',encoding='utf-8') as file:
                                    deleteObj = {
                                        'Delete': deleteNum
                                    }
                                    json.dump(deleteObj,file)
                                print('Your event has been deleted.')
                        # ask to return to home page
                        returnHome = input('Return to Home Page? (y/n): ')
                        if returnHome == 'y':
                            goHome = True
                # enter the forum page
                enterForum = input('Would you like to enter the Forum Page (y/n): ')
                if enterForum == 'y':
                    while goHome is False:
                        openingMessage = '''
                        Welcome to the event forum page. Here you will be able to comment on
                        any listed event.
                        '''
                        print(textwrap.dedent(openingMessage))
                        print()
                        makePost = input('Want to comment on an event? (y/n): ')
                        if makePost == 'y':
                            with open('events.txt', 'r', encoding='utf-8') as eventFile:
                                eventData = json.load(eventFile)
                            print()
                            for eventName in eventData:             # print out only name and date
                                eventDict = eventData[eventName]
                                print('Event Number: ', eventDict['Event Number'])
                                print('Event: ', eventDict['name'])
                                print('Date:', eventDict['date'])
                                print()
                            eventNum = input('Which event would you like to comment on? (enter number): ')
                            print('Go ahead a write a comment below: ')
                            print()
                            userComment = input()
                            # make a post request
                            with open('ForumReceive.txt','w',encoding='utf-8') as file:
                                postObj = {
                                    "Event Number": eventNum,
                                    "Post": userComment,
                                    "username": username
                                }
                                json.dump(postObj,file)
                            print(f"Your comment has been submitted to the Event Number {eventNum} forum")
                            print()
                        # read posts section
                        readPost = input('Want to read posts made about an event? (y/n): ')
                        if readPost == 'y':
                            with open('events.txt', 'r', encoding='utf-8') as eventFile:
                                eventData = json.load(eventFile)
                            print()
                            for eventName in eventData:
                                eventDict = eventData[eventName]
                                print('Event Number: ', eventDict['Event Number'])
                                print('Event: ', eventDict['name'])
                                print('Date:', eventDict['date'])
                                print()
                            readEventNum = input('Read posts about which event? (enter number): ')
                            # make a read request
                            with open('ForumReceive.txt','w',encoding='utf-8') as file:
                                readReq = {
                                    "Event Number": readEventNum,
                                    "Read": "Read"
                                }
                                json.dump(readReq, file)
                            time.sleep(3)
                            # open and print received posts
                            with open('ForumReceive.txt', 'r', encoding="utf-8") as Readfile:
                                readObj = json.load(Readfile)
                                if "N/A" not in readObj:
                                    postObjs = readObj[readEventNum]
                                    postCount = 0
                                    for post in postObjs:
                                        if postCount == 0:
                                            eventName = post['Name']
                                            eventDate = post['Date']
                                            print(f'Below are comments regarding Event: {eventName} Date: {eventDate}')
                                            print()
                                            postCount += 1
                                        print('User: ', post['username'])
                                        print('Comment: ', post['Post'])
                                        print()
                                else:
                                    print("Sorry there are no posts for this event yet")
                        # ask to return to home page
                        returnHome = input('Return to Home Page? (y/n): ')
                        if returnHome == 'y':
                            goHome = True
                # enter job list page
                enterJobList = input('Would you like to enter the job list page? (y/n): ')
                if enterJobList == 'y':
                    welcomeMessage = '''
                    Hello, this is the Event Job List page. Here you can crete job listings
                    for events you created or take on a job for any available listing.
                    '''
                    print(textwrap.dedent(welcomeMessage))

                    postJob = input('Would you like to list a job for an event you created? (y/n): ')
                    # print out all of a user's created events
                    userEventNums = []
                    with open('EventDelete.txt', 'r', encoding='utf-8') as file:
                        eventObjs = json.load(file)
                        print('Below are the events that you have created:')
                        for event in eventObjs:
                            currentNum = int(event)
                            userEventNums.append(currentNum)  # create a list of a user's events
                            currentEvent = eventObjs[event]
                            print('Event Number: ', currentEvent['Event Number'])
                            print('Event: ', currentEvent['name'])
                            print('Date:', currentEvent['date'])
                            print('Description: ', currentEvent['description'])
                            print()
                    eventNum = input('What event do you want to create a job listing for? (enter number):  ')
                    userEventNums = str(userEventNums)
                    while eventNum not in userEventNums:
                        print('ERROR: The Event Number you have entered is invalid.')
                        eventNum = input('Please enter the "Event Number" of the event you want to list a job about: ')
                    jobTitle = input('Enter Job Title: ')
                    print('Enter the Job Description below:')
                    jobDesc = input()
                    submitJob = input('Are you sure you want to create this job listing? (y/n): ')
                    if submitJob == 'y':
                        # create a request to post job































