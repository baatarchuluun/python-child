# 1.	n натурал тоо өгөгдөв. 
    # i)	2^n-г ол. s = 2 * 2 * ...* 2 (n удаа)
    # ii)	(1+1/1^2)*(1+1/2^2) … *(1+1/n^2)
n = int(input("n:"))
s = 1
for i in range(1, n+1):
    s *= 2
print(s)

s = 1
for i in range(1, n+1):
    s *= (1 + 1/i ** 2)

print(s)