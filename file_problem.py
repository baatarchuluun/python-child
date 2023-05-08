a = int(input("a: "))
b = int(input("b: "))

fp = open("answer.txt", "a")
fp.write("a = " + str(a) + "\n")
fp.write("b = " + str(b) + "\n")
c = a + b
fp.write("c = " + str(c) + "\n")
fp.close()