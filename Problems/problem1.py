# Бодлого 1: Гараас оруулсан 3 тоо (a, b, c) 
# гурвалжны талууд болох эсэхийг хэвлэдэг 
# програм бич.
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a + b > c and a + c > b and b + c > a:
    print("Triangle")
else:
    print("Not triangle")