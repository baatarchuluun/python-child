fp = open("input.txt", "r")
n = int(fp.read())
fp.close()

s = n * (n + 1) / 2

fp2 = open("output.txt", "w")
fp2.write(str(s))
fp2.close()