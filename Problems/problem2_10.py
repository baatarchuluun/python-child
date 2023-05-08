# 10. Өгөгдсөн тооны цифрүүд нь буурах дараалал үүсгэх эсэхийг шалга.
n = int(input("n="))

m = []
while n > 0:
    r = n % 10
    n = n // 10
    m.append(r)

min = m[0]
ind = 0
for i in m:
    if i < min:
        ind = 1
        print("Buurah daraalal bish")
        break

if ind == 0:
    print("Buurah daraalald bn")