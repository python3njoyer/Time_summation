import csv
import datetime as dt

courses = {}

with open('Media_Production_Overview.csv', 'r') as readfile:
    timesheet = csv.reader(readfile)
    next(timesheet)
    for row in timesheet:
        if row[0] != '':
            courses[row[0]] = []
            for columns in range(1,4):
                courses[row[0]].append(row[columns])


def time2Seconds(time):
    time = time.split(':')
    h = int(time[0])*3600
    m = int(time[1])*60
    return h + m + int(time[2])


def seconds2Time(seconds):
    h = seconds//3600
    m = (seconds%3600) // 60
    s = (seconds%3600) % 60
    return(str(h) + ":" + str(dt.time(0, m, s))[3:])


def sum_times(dict):
    for code in dict:
        totalTime = 0  # convert 0 to 0 seconds if using timedelta
        for times in dict[code]:
            times = times.split(', ')
            for time in times:
                if time != '':
                    time = time2Seconds(time)
                    totalTime += time
        print(seconds2Time(totalTime))


sums = sum_times(courses)
