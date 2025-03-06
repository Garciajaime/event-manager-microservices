import json


def findEvent(eventNum):
    '''
    Finds the event name and date based on the
    event number
    :param eventNum: used to find name
    :return: event name and date
    '''
    with open('events.txt','r',encoding='utf-8') as eventsFile:
        eventsObj = json.load(eventsFile)
        for NumKey in eventsObj:
            if NumKey == eventNum:
                event = eventsObj[NumKey]
                eventName = event['name']
                eventDate = event['date']
                eventTuple = (eventName,eventDate)
        return eventTuple


while True:
    try:
        with open('ForumReceive.txt','r',encoding='utf-8') as file:
            requestMessage = json.load(file)
    except json.JSONDecodeError:
        pass
    else:
        if "Post" in requestMessage:
            print("A post request has been made...")
            with open('ForumPosts.txt','r',encoding='utf-8') as postFile:
                forumData = json.load(postFile)
                # create post object
                eventNum = requestMessage['Event Number']
                eventName, eventDate = findEvent(eventNum)
                userName = requestMessage['username']
                postData = requestMessage['Post']
                postObj = {
                    "username": userName,
                    "Post": postData,
                    "Name": eventName,
                    "Date": eventDate

                }
                # append post object to forum list object
                forumData[eventNum] = postObj
            # update the forum text file
            with open('ForumPosts.txt','w',encoding='utf-8') as postFile:
                json.dump(forumData,postFile,indent=4)
            # clear the text file of any requests
            open('ForumReceive.txt', 'w').close()
            print('Post request has been submitted...')
        elif 'Read' in requestMessage:
            eventNum = requestMessage['Event Number']
            print(f'A read request for Event Number "{eventNum}" has been made...')
            # get all posts made about requested event
            with open('ForumPosts.txt','r',encoding='utf-8') as forumFile:
                forumData = json.load(forumFile)
                eventPosts = {}
                for numKey in forumData:
                    forumObj = forumData[numKey]
                    username = forumObj['username']
                    userPost = forumObj['Post']
                    if numKey == eventNum:
                        eventPosts[username] = userPost
            # send object via text file pipline
            with open('ForumReceive.txt','w',encoding='utf-8') as sendFile:
                json.dump(eventPosts,sendFile,indent=4)
            # clear the text file of any requests
            #open('ForumReceive.txt', 'w').close()
            print('Post data has been sent...')









