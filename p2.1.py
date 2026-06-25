Tuple1 = ("Shreyash Kadam", 90)
Tuple2 = ("Om Wala", 122)
nested_tuple = (Tuple1, Tuple2,)
print("Nested Tuple:", nested_tuple)


sorted_subjects = sorted(nested_tuple, key=lambda x: x[1])
print("Sorted Subjects (by subject code):", sorted_subjects)


copy1 = nested_tuple[:]
copy2 = list(nested_tuple)
print("Original List:", nested_tuple)
print("Copy using slicing:", copy1)
print("Copy using list():", copy2)

try:
    nested_tuple[0][1] = 999
except TypeError as e:
    print("\nTuple Immutability Test: Error occurred ->", e)

