# Бодлого 2. Гараас оруулсан 3 тоо (a, b, c) 
# тэгш өнцөгт гурвалжин мөн эсэхийг хэвлэдэг 
# програм бич.
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a**2 + b**2 == c**2:
    print("Tegsh untsugt mun")
elif c*c + b*b == a*a:
    print("Tegsh untsugt mun")
elif a*a + c*c == b*b:
    print("Tegsh untsugt mun")
else:
    print("Tegsh untsugt bish")