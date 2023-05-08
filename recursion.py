def calc_sum(n):
    if n == 1:
        return 1
    else:
        return n + calc_sum(n - 1)

print(calc_sum(100))





def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

sum = calc_sum(3)
print(sum)

fact = factorial(5)
print(fact)