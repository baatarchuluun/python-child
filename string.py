my_string = "Ulaanbaatar"
print(my_string[1])

for ch in my_string:
    print(ch, end=" ")
print()
print("Length: ", len(my_string))
print("My " + my_string)

print(my_string.upper())
print(my_string.lower())
print("i love u".capitalize())

print(my_string.count("a"))

text = ['Python', 'is', 'a', 'programming', 'language']
text2 = ' '.join(text)
print(text2)

print(text2.find('programming'))

a = "123"
if a.isnumeric():
    print("This is numberic")
else:
    print("This is text")

text3 = text2.replace("Python", "Java")
print(text3)