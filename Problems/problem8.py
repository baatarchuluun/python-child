month_days = (0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)

def leap_year(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return True
    return False

def duration(year, month, day, ind):
    s2 = 365
    s = month_days[month] + day
    if leap_year(year) and month > 2: s += 1
    if leap_year(year): s2 = 366
    if ind == 1: return s
    return s2 - s

y = int(input("Year="))
m = int(input("Month="))
d = int(input("Day="))

y1 = int(input("Year1="))
m1 = int(input("Month1="))
d1 = int(input("Day1="))

leap_year_count = 0
for y2 in range(y, y1 + 1):
    if leap_year(y2):
        leap_year_count += 1
    
s = (y1 + 1 - y) * 365 + leap_year_count
s = s - (duration(y, m, d, 1) + duration(y1, m1, d1, 2))

print("{} days are between {}-{}-{} and {}-{}-{}".format(s, y, m, d, y1, m1, d1))