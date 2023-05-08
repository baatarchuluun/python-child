# Datetime module
import datetime as dt
#x = dt.datetime.now()
x = dt.datetime(2022, 11, 1, 10, 15, 3, 92982)
print(x)
print(x.strftime("%A")) # Saturday
print(x.strftime("%a")) # Sat
print(x.strftime("%w")) # 6
print(x.strftime("%d")) # 1-31
print(x.strftime("%b %B")) # Dec December
print(x.strftime("%m")) # month 12
print(x.strftime("%y %Y")) # year 22 2022
print(x.strftime("%H %I %p")) # 12 12 AM/PM
print(x.strftime("Minutes: %M")) # minutes
print(x.strftime("Seconds: %S")) # seconds
print(x.strftime("%f")) # microseconds
print(x.strftime("%z")) # timezone
print(x.strftime("%j")) # n-th day
print(x.strftime("%U %W")) # n-th week
print(x.strftime("%C")) # century
print(dt.MAXYEAR, dt.MINYEAR) # max and min year