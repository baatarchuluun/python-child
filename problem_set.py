set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

def set_max(given_set):
    i = 0
    for el in given_set:
        if i == 0: m = el
        if el > m:
            m = el
        i = i + 1
    return m
m1 = set_max(set1)
m2 = set_max(set2)
sum = m1 + m2
print("Sum =", sum)