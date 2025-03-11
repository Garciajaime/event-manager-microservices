# Lorraine Byrne
#CS 361
# Microservice A for Abraham's Main Event App Project
# References
# https://pypi.org/project/holidays/
# https://www.geeksforgeeks.org/python-holidays-library/
# https://stackoverflow.com/questions/70391399/datetime-datatime-strptimedate-y-m-d-adds-000000-for-different-dates

import time
import holidays
import datetime

# defines which country you are going to use for the holidays package
us_holidays = holidays.US()

if __name__ == '__main__':
    while True:
        try:
            # opens the personal calendar to check the date
            # sees if the date is in the right format
            # if not, an error text will pop up
            with open("personal-calendar.txt", "r") as file:
                line = file.readline().strip()

            event_date = datetime.datetime.strptime(line, "%Y-%m-%d").date()

            # If event is in the holiday package,
            # then it will write onto the holiday-note.txt "Yes" and day what holiday it is
            # if the event is not, it will write into the text "No" the date is not a holiday
            if event_date in us_holidays:

                print(f"{event_date} is a holiday: {us_holidays[event_date]}")
                with open("holiday-note.txt", "w") as file:
                    file.write(
                        f"Yes\n{event_date} is a holiday: {us_holidays[event_date]}")
                time.sleep(5)
                # clear files
                open('personal-calendar.txt','w').close()
                open('holiday-note.txt','w').close()

            else:
                print(f"{event_date} is not a holiday")
                with open("holiday-note.txt", "w") as file:
                    file.write(f"{event_date} is not a holiday")
                # clear file
                open('personal-calendar.txt', 'w').close()
        except ValueError:
            pass
            #print("Invalid date format in file. Expected YYYY-MM-DD.")
            #open('personal-calendar.txt', 'w').close()  # clear file
