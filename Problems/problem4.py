# n натурал тоо өгөгдөв (n>99). 
# Энэ тоонд 100 хэд дахин багтсаныг ол.
n = int(input("n = "))
if n <=99:
    print("n must be greater than 99")
else:
    s = 0
    while n > 99:
        n -= 100
        s += 1
    print(s)