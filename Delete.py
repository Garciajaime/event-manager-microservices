import json

while True:
    # listen for Deletion/Read requests
    try:
        with open('EventDelete.txt','r',encoding='utf-8') as file:
            request_message = json.load(file)
    except json.JSONDecodeError:
        pass
    else:
        if 'Delete' in request_message:
            # get number of event for deletion
            delete_num = request_message['Delete']
            print(f'Request to delete Event Number: {delete_num}')
            # delete event from event list
            with open('events.txt','r',encoding='utf-8') as event_file:
                events_obj = json.load(event_file)
                events_obj.pop(str(delete_num))
            with open('events.txt','w',encoding='utf-8') as delete_event_file:
                json.dump(events_obj,delete_event_file,indent=4)
            # clear the text file of any requests
            open('EventDelete.txt', 'w').close()
            print(f'Event Number {delete_num} has been deleted')
        if 'Read' in request_message:
            # get username
            requestUsername = request_message['Read']
            userEvents = {}
            print(f"A request has been made for {requestUsername}'s events")
            with open('events.txt', 'r', encoding='utf-8') as readFile:
                eventObjs = json.load(readFile)
                for event in eventObjs:
                    currentEvent = eventObjs[event]
                    eventUsername = currentEvent['username']
                    # create an object of all the users events
                    if eventUsername == requestUsername:
                        userEvents[event] = currentEvent
            # add newly created user events object to text file
            with open('EventDelete.txt','w',encoding='utf-8') as sendFile:
                json.dump(userEvents,sendFile,indent=4)
            print('Your events have been sent...')




