def express(n):
    if n == 1:
        return 2
    else:
        x = (1 + 1 / (n * n))
        return  x * express(n - 1)
print(express(10))