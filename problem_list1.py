# solution 1
tuple1 = (1, 3, 5, 6, 8)
tuple1 = tuple1 + (9,)
print(tuple1)

# solution 2
list1 = list(tuple1)
list1.append(9)
tuple1 = tuple(list1)
print(tuple1)

list1 = [1, 2, 3, 5, 7, 8, 10, 20, 21, 23]
def isPrime(n):
    s = 0
    for i in range(1, n + 1):
        if n % i == 0:
            s = s + 1
    if s == 2:
        return True
    return False    

list2 = []
for i in list1:
    if isPrime(i):
        list2.append(i)

print(list2)