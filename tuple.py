# tuple
my_tuple = (-5, 6, 10, 0, 6, 1, [100, 101])
print(my_tuple)

print(type(my_tuple))
my_tuple2 = (10, 20) + my_tuple
print(my_tuple2)
print(my_tuple[2]) # positive index
print(my_tuple[-1]) # negative index

print(my_tuple[1:4]) # slice
print(2 * my_tuple)

print(my_tuple[6][1])
print("Length: ", len(my_tuple))

my_tuple3 = (-5, 6, 10, 0, 6, 1)
print("Max: ", max(my_tuple3))
print("Min: ", min(my_tuple3))
print("Sum: ", sum(my_tuple3))
print(sorted(my_tuple3))
print(my_tuple3.count(6))
print(my_tuple3.index(10))