# 8. 6 оронтой тооны эхний гурван цифрүүдийн нийлбэр сүүлчийн гурван цифрүүдийн 
# нийлбэртэй тэнцүү байвал түүнийг азын тоо гэдэг. Жишээ нь 100010, 2100003 нь азын тоо юм. 
# Бүх азын тоог ол.
for i in range(100000,1000000):
    a=i//100000
    b=(i%100000)//10000
    c=(i%10000)//1000
    d=(i%1000)//100
    e=(i%100)//10
    f=i%10
    g=a+b+c
    h=d+e+f
    if g==h:
        print(i, end=' ')