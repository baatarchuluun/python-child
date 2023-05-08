# 4. Хоёр оронтой бүх тоог дарааллуулан бичжээ. Тэгвэл уг дарааллын k дахь цифрийг ол.
# 1011121314151617.....9596979899
myString = ''
for i in range(10, 100):
    myString += str(i)

k = 10
print(myString[k - 1])

# luuya's solution
digit = [0]
for i in range(10, 100):
    r = i // 10
    digit.append(r)
    r2 = i % 10
    digit.append(r2)

print(digit[k])