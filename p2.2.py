my_tuple = (90, 122, 88, 84, 129)
print("Original Tuple:", my_tuple)

print("First Element:", my_tuple[0])
print("Last Element:", my_tuple[-1])

middle_tuple = my_tuple[1:4]
print("Middle 3 Elements:", middle_tuple)


tuple1 = (90, 122, 88)
tuple2 = (84, 129, 127)
concatenated = tuple1 + tuple2
print("Concatenated Tuple:", concatenated)


reversed_tuple = my_tuple[::-1]
print("Reversed Tuple:", reversed_tuple)

count_tuple = (90, 122, 90, 88, 84, 129, 90)
count = count_tuple.count(90)
print("Count of 90:", count)

index = count_tuple.index(90)
print("Index of 4:", index)

element = 90
if element in count_tuple:
    print(element, "exists in the tuple")
else:
    print(element, "does not exist in the tuple")

my_list = [90, 122, 88,84]
converted_tuple = tuple(my_list)
print("Tuple converted from list:", converted_tuple)

num_tuple = (90, 122, 84, 88, 129, 120)
sorted_tuple = tuple(sorted(num_tuple))
print("Sorted Tuple:", sorted_tuple)

repeated_tuple = tuple1 * 3
print("Repeated Tuple:", repeated_tuple)

try:
    my_tuple[0] = 99
except TypeError as e:
    print("Tuple is immutable:", e)
