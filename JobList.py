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
                # create post object
                jobPost = {
                    'Job Title': jobTitle,
                    'Job Description': jobDesc
                }
                # append post to post list if event posts already exist
                if eventNum in jobPostsObjs:
                    jobList = jobPostsObjs[eventNum]
                    jobList.append(jobPost)
                else:
                    jobPostsObjs[eventNum] =  [jobPost] # create new list for jobs
            # post object to the forum
            with open('JobPosts.txt','w',encoding='utf-8') as postFile:
                json.dump(jobPostsObjs,postFile)
            time.sleep(1)
            print("Job has been posted...")
            open('JobReceive.txt','w').close()  # clear file

