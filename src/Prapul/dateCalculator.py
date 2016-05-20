def checkDate(date):
    date = str(date)
    # check format
    if len(date) != 10:
        print "incorrect format"
        return 0, 0, 0

    # check year
    year = date[0:4]
    if (not year.isdigit()) or int(year) < 0:
        print "incorrect year"
        return 0, 0, 0

    # check month
    month = date[5:7]
    if (not month.isdigit()) or int(month) > 12 or int(month) < 1:
        print "incorrect month"
        return 0, 0, 0

    # check day
    day = date[8:]
    if (not day.isdigit()) or int(day) > 31 or int(day) < 1:
        print "incorrect day"
        return 0, 0, 0

    return int(year), int(month), int(day)


def getDay(date):

    year,month,day = checkDate(date)
    if month == 0:
        return "Incorrect input"

    for i in range(1,year):
        if i%4 == 0 and (i%100 != 0 or i%400 == 0):
            day += 366
        else:
            day += 365

    monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        monthdays[1] = 29
    for i in range(0,month-1):
        day += monthdays[i]

    weekday = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}

    return weekday[day % 7]


print getDay("2016-05-20")