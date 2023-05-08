def add(x, y):
    result = x + y
    return result

def subtract(x, y):
    if x > y:
        result = x - y
    else:
        result = y - x
    return result

def add_subtract(x, y):
    r1 = add(x, y)
    r2 = subtract(x, y)
    return r1, r2

s1 = add(10, 15)
s2 = subtract(10, 15)
print("Sum =", s1)
print("Subtract =", s2)
x1, x2 = add_subtract(30, 20)
print(x1, x2)