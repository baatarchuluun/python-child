n = int(input("n = "))
m = int(input("m = "))

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

print(gcd_value)