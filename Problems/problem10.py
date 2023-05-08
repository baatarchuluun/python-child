n = int(input("n="))
s2 = 0
for i in range(1, n + 1):
    s = 1
    for j in range(i, 2*i + 1):
        s *= j
    s2 += s
print(s2)