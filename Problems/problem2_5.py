# 5. Хүний төрсөн он сар өдөр ба өнөөдрийн он сар өдөр өгөгдсөн бол уг хүн хэдэн настайг ол. 
# Төрсөн сард нь хүрээгүй байвал нас нэмсэнд тооцохгүй.
y=int(input("year="))
m=int(input("mounth="))
d=int(input("day="))
y1=int(input("now,year="))
m1=int(input("now,mounth="))
d1=int(input("now,day="))
age = y1 - y
if m1 < m:
    age -= 1
print("Nas: " + age)