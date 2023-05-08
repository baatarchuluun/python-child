# шинэ файл үүсгэх
#fp = open("my_test.txt", "x")
#fp.close()

# файлаас өгөгдөл унших
fp = open("my_test.txt", "r")
#print(fp.read())
# эхний 5 тэмдэгт
print(fp.read(5))
# эхний мөрийг авна
line = fp.readline()
cnt = 1
while line:
    print("Line {}: {}".format(cnt, line.strip()))
    line = fp.readline()
    cnt += 1
fp.close()
