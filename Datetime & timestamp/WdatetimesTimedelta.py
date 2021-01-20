from datetime import datetime, timedelta
import time

# to print todays date
todaysdate = datetime.now()
print(todaysdate)

# Creating a custom date or datetime
customtime = datetime(2018, 5, 2, 15, 14)
print(customtime)

# Converting date in string format from either a source file or by user input to Datetime
dtConv = datetime.strptime("2020/05/01", "%Y/%m/%d")
print(dtConv)

# Converting datetime into a string format
dateconversion1 = dtConv.strftime("%Y/%m/%d")
print(dateconversion1)

# Coverting a TimeStamp into a Datetime object
Atimestamp = time.time()
dt1 = datetime.fromtimestamp(Atimestamp)
print(dt1)

# Creating formatted string with datetime

print(f"{dtConv.year}/{dtConv.month}")

# datetime comparism

print(todaysdate > customtime)


# working with timedelta(days,seconds difference) .This mainly has to do with datetime difference = timedelta

duration = customtime-dtConv
print("days:", duration.days)
print("seconds:", duration.seconds)
print("Total seconds:", duration.total_seconds())

# to increament dateTime with timedelta
mydate = datetime.now() + timedelta(days=1, seconds=1000)
print(mydate)
