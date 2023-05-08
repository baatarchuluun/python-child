# 5. n натурал тоо өгөгдөв (n<=99). Энэ тооны 
# цифрүүдийн куб-уудын нийлбэр нь n-ийн квадраттай 
# тэнцүү эсэхийг шалга.
def cub(n):
    a = n // 10
    b = n % 10
    if a*a*a + b*b*b == n*n:
        return True
    return False

for i in range(10, 100):
    if cub(i) == True:
        print(i)