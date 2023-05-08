fp = open("data/input2.txt", "r")
line = fp.readline()
my_list = []
my_list.append(int(line))
while line:
    line = fp.readline()
    if line != '':
        number = int(line)
        my_list.append(number)
s = sum(my_list)
fp1 = open("data/output.txt", "a")
fp1.write(str(s)+'\n')
fp1.close()
print(my_list)