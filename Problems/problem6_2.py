n = int(input("n = "))
m = int(input("m = "))

z = n * m
if m > n:
    n, m = m, n

while m > 0:
    r = n % m
    if r == 0:
        gcd_value = m
        break
    else:
        n = m
        m = r

hbeh = z / gcd_value

print(hbeh)