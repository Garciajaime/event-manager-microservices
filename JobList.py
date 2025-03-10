import json
import time

while True:
    try:
        with open('JobReceive.txt','r', encoding='utf-8') as file:
            requestMessage = json.load(file)
    except json.JSONDecodeError:
        pass
    else:
        if 'Post' in requestMessage:
            print("A post request has been made...")
            with open('JobPosts.txt','r',encoding='utf-8') as jobFile:
                jobPostsObjs = json.load(jobFile)
                eventNum = requestMessage['Event Number']
                jobTitle = requestMessage['Job Title']
                jobDesc = requestMessage['Job Description']
                jobAvail = requestMessage['Availability']
                # create post object
                jobPost = {
                    'Job Title': jobTitle,
                    'Job Description': jobDesc,
                    'Availability': jobAvail
                }
                # append post to post list if event posts already exist
                if eventNum in jobPostsObjs:
                    jobList = jobPostsObjs[eventNum]
                    jobList.append(jobPost)
                else:
                    jobPostsObjs[eventNum] = [jobPost]  # create new list for jobs
            # post object to job listings
            with open('JobPosts.txt','w',encoding='utf-8') as postFile:
                json.dump(jobPostsObjs,postFile, indent=4)
            time.sleep(1)
            print("Job has been posted...")
            open('JobReceive.txt','w').close()  # clear file
        if "Read" in requestMessage:
            print("A read request has been made...")
            eventNum = requestMessage["Event Number"]
            with open('JobPosts.txt','r',encoding='utf-8') as readFile:
                jobPostsObj = json.load(readFile)
                postObj = {}
                for key in jobPostsObj:
                    if key == eventNum:
                        jobList = jobPostsObj[key]
                        postObj[eventNum] = jobList
            time.sleep(3)
            with open('JobReceive.txt','w',encoding='utf-8') as sendFile:
                json.dump(postObj,sendFile,indent=4)
            print("Your job list has been sent...")
        if "Take Job" in requestMessage:
            print("Request to take a job...")
            eventNum = requestMessage["Event Number"]
            reqJobTitle = requestMessage["Job Title"]
            reqUser = requestMessage["username"]
            # find job post and change availability
            with open('JobPosts.txt','r',encoding='utf-8') as jobPostFile:
                jobsObj = json.load(jobPostFile)
                # find event object
                for event in jobsObj:
                    if event ==  eventNum:
                        eventList = jobsObj[event]
                        # find job within list
                        for job in eventList:
                            eventJobTitle = job["Job Title"]
                            if eventJobTitle == reqJobTitle:
                                job["Availability"] = f'Taken by user: {reqUser}'
            # update job posts
            with open('JobPosts.txt','w',encoding='utf-8') as editFile:
                json.dump(jobsObj,editFile,indent=4)
            open('JobReceive.txt', 'w').close()  # clear file
            time.sleep(3)
            print(f"Your request to take this job: {reqJobTitle} has been submitted...")




