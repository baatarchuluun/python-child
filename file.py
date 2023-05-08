import os
#fp = open('test.txt', 'w')
#fp.write('first line')
#fp.close()

fp = open("test.txt", "r")
#text = fp.read()
#print(text)

#text2 = fp.read(10)
with open("test.txt") as fp:
   line = fp.readline()
   cnt = 1
   while line:
       print("Line {}: {}".format(cnt, line.strip()))
       line = fp.readline()
       cnt += 1
fp.close()

with open("test.txt", "w") as fp:
    fp.write("This is append text")

fp.close()

if os.path.exists("delete-file.txt"):
    os.remove("delete-file.txt")
else:
    print("The file does not exist")
