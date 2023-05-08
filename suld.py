# this is comment
a = 10
b = 25
c = a + b
print("Sum of two numbers: ", c)
# int -> integer
# float -> butarhai
# string - temdegt
text = "Ulaanbaatar"
print(type(text))

d = float(c)
print(type(d))

# arithmetic +, -, *, /, %, //
c = b - a
print(c)

c = a * b
print("Multiply:", c)

c = a / b
print("Divide: ", c)

r = b % a
print("Remainder:", r)

print("Buhel: ", b // a)

k = (a + b) / a + c * a
print("k =", k)

# boolean expression - logic ilerhiilel: True/False
# >, <, >=, <=, ==, !=
if a > b:
    print("a is greater than b")
elif a == b:
    print("a and b are equal")
else: 
    print("b is greater than a")
    
gpa = 59
if gpa >= 90:
    print("A")
elif gpa >= 80:
    print("B")
elif gpa >= 70:
    print("C")
elif gpa >= 60:
    print("D")
else:
    print("F")

# 365, 366
year = 2300
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("This year is leap year")
else:
    print("This year is regular year")

