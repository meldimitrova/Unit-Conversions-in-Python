# @author Melina Dimitrova

# DateTime functions

import datetime

## Print the weekday by given date
def day():
    intDay = datetime.date(year=2008, month=12, day=3).weekday()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
        "Sunday"]
    print(days[intDay])
    print("Python 3 was released on a " + days[intDay])

## Function with given string
    dt = '21/03/2012'
    day, month, year = (int(x) for x in dt.split('/'))
    ans = datetime.date(year, month, day)
    print (ans.strftime("%A"))

# with user input
    date_input = input("Please write a date in the format dd/mm/yyyy ")
    d, m, y = (int(x) for x in date_input.split('/'))
    a = datetime.date(y, m, d)
    print ("The weekday was a " + a.strftime("%A"))

day()

# Calendar function

import calendar

def cal():
    yy = 2022
    mm = 12

# display the calendar
    print("Calendar :\n" + calendar.month(yy, mm))

    y = input("Write a year in a format yyyy ")
    m = input("Write a month in a format mm ")
    year = int(y)
    month = int(m)

    print("Your calendar :\n" + calendar.month(year, month))

cal()
