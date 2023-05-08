# n-дэхь fibonacci тоог олох функц
def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)
# эхний 15 fibonacci тоог хэвлэх
for i in range(1, 16):
    print(fibo(i), end=" ")