
def getDay(date):
    weekday = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}
    year = date[0:4]
    month = date[5:7]
    day = date[8:]

    return day

print getDay("2016-20-05")