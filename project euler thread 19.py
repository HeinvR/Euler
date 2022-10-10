import datetime
from datetime import date, timedelta

totalsundays = 0
td = timedelta(days=1)
startdate = datetime.date(1901, 1, 1)
enddate = datetime.date(2000, 12, 31)

while startdate <= enddate:
    if startdate.weekday() == 6 and startdate.day == 1:
        totalsundays += 1
    startdate += td

print(totalsundays)
