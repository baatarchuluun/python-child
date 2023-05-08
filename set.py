# set-ийг зарлах
sample_set = {"Mike", 20, 3.14}
print(sample_set)
print(type(sample_set))

# element-үүдийг авах
for value in sample_set:
    print(value)
# list-ээс set үүсгэх
number_list = [20, 30, 20, 30, 50, 30]
sample_set = set(number_list)
print(sample_set)
# хоосон set үүсгэх
empty_set = set()
print(type(empty_set))

book_set = {"Harry Potter", "Sophie's word", 
"Robinson Cruso"}
if "Harry Potter" in book_set:
    print("This book does exist")
else:
    print("This book doesn't exist")    

print("Number of books:", len(book_set))
# 1 элемент нэмэхдээ .add функцийг ашиглана
book_set.add("Ulysses")
print(book_set)
# 2 ба түүнээс дээш элементийг нэмэхдээ .update
# функцийг ашиглана
book_set.update(["Tungalag Tamir", "Word"])
print(book_set)
# set-ээс элемент устгах
book_set.discard("Word")
print(book_set)
# book_set.remove("Word")
# pop нь random-оор устгана
book_set.pop()
print(book_set)
# clear нь set-ийг хоосолдог
sample_set.clear()
print(sample_set)
# del нь set-ийг устгана
# del empty_set
color_set = {"violet", "indigo", "blue", "green",
"yellow"}
remain_set = {"indigo", "orange", "red"}
# union
new_set = color_set | remain_set
print(new_set)
new_set = color_set.union(remain_set)
print(new_set)
# intersection
new_set = color_set & remain_set
print(new_set)
new_set = color_set.intersection(remain_set)
print(new_set)
# difference
new_set = color_set - remain_set
print(new_set)
new_set = color_set.difference(remain_set)
print(new_set)

sample_set = {100, 20, 30, 50}
print("Max:", max(sample_set))
print("Min:", min(sample_set))

color_set2 = color_set.copy()
color_set3 = set(color_set)
color_set4 = color_set
print(color_set2, color_set3, color_set4)
# subset
print(color_set.issubset({"indigo", "blue"}))
print({"indigo", "blue"}.issubset(color_set))
# superset
print(color_set.issuperset({"indigo", "blue"}))
print({"indigo", "blue"}.issuperset(color_set))
