import math
def sqrt_v2(n):
    if n == 1:
        return math.sqrt(2)
    else:
        return math.sqrt(2 + sqrt_v2(n - 1))
print(sqrt_v2(2))