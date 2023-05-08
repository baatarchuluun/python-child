def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n - 2) + fibo(n - 1)
# эхний 20 фибоначчийн тоог хэвлэх
for i in range(1, 21):
    print(fibo(i), end=" ")