def checkDate(date):
    '''
    checks whether the date in the format yyyy-mm-dd is valid and returns the year, month and day
    :param :date(str)
    :return: year(int), month(int), day(int)
    '''
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
    year = int(year)

    # check month
    month = date[5:7]
    if (not month.isdigit()) or int(month) > 12 or int(month) < 1:
        print "incorrect month"
        return 0, 0, 0
    month = int(month)

    # check day
    monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        monthdays[1] = 29

    day = date[8:]
    if (not day.isdigit()) or int(day) > monthdays[int(month)-1] or int(day) < 1:
        print "incorrect day"
        return 0, 0, 0
    day = int(day)

    return year, month, day

def duration(date1,date2):
    '''

    :param date1:(str) first date in the format yyyy-mm-dd
    :param date2:(str) second date in the format yyyy-mm-dd
    :return: the number of days in between the two dates
    '''
    year1, month1, day1 = checkDate(date1)
    year2, month2, day2 = checkDate(date2)

    # making sure that date1 is earlier than date2
    if year2<year1:
        return "date1 is later than date2"
    if year2 == year1 and month2<month1:
        return "date1 is later than date2"
    if year2 == year1 and month2 == month1 and day2<day1:
        return "date1 is later than date2"
    day=0

    # the number of days in the year difference is added to the day depending on whether or not it is a leap year
    for i in range(year1, year2):
        if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
            day += 366
        else:
            day += 365

    # difference in the number of days between the months is added or subtracted based on which month is greater
    monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year2 % 4 == 0 and (year2 % 100 != 0 or year2 % 400 == 0):
        monthdays[1] = 29
    if month2>month1:
        for i in range(month1-1, month2 - 1):
            day += monthdays[i]
    else:
        for i in range(month2 - 1, month1 - 1):
            day -= monthdays[i]

    #difference in days is added
    day += (day2-day1)

    return day

print duration(raw_input("enter the first date (yyyy-mm-dd): "),raw_input("enter the second date (yyyy-mm-dd): "))