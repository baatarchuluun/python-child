# 1. Өгөгдсөн натурал тооны бүх хуваагчийн тоо ба тэдгээрийн нийлбэрийг ол.
n = int(input("n: "))
s = 0 # хуваагчуудын нийлбэр
m = 0 # хуваагчийн тоо
for i in range(1, n):
    if n % i == 0:
        s += i
        m += 1
        print(i, end=' ')
    
print("huvaagchiin too: {}, huvaagchuudiin niilber: {}".format(m, s))