def checkDate(date):
    """
    :param date: str in format yyyy-mm-dd
    :return: year, month, day (int)
    checks whether date is valid and returns year, month and day
    """
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


def getDay(date):
    """
    :param date: str in yyyy-mm-dd
    :return: the day of the week on which date falls

    """
    # date is checked for correct format and monthyear and day extracted from it
    year,month,day = checkDate(date)
    if month == 0:
        return "Incorrect input"

    # For every year since the latest 400th year total number of days of that year is added to the day depending on whether or not it is a leap year
    for i in range(1,year%400):
        if i%4 == 0 and i%100 != 0:
            day += 366
        else:
            day += 365

    # For every month after January total number of days in that month is added to the day
    monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        monthdays[1] = 29
    for i in range(0,month-1):
        day += monthdays[i]

    # dictionary to translate weekday from integer to string
    weekday = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}

    return weekday[day % 7]


print getDay(raw_input("Enter date in the format yyyy-mm-dd : "))