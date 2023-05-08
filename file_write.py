import os
# file_write.py
#fp = open("my_test2.txt", "w")
#fp.write("This is written text")
#fp.close()

fp2 = open("my_test2.txt", "a")
fp2.write("This is appended text")
fp2.close()

if os.path.exists("delete-file.txt"):
    os.remove("delete-file.txt")
else:
    print("The file is does not exist")