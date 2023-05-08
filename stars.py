n = 4
i = 1
while i < (n*2 + 1):
    if i < n + 1:
        print(i * "*")
    else:
        print((n * 2 - i) * "*")    
    i = i + 1

for i in range(1, n + 1):
    print(i * "*")
for i in range(1, n):
    print((n - i) * "*")  