import numpy as np

print("Shreyash Kadam S091")

arr = np.array([155, 169, 82, 124])

print("4a. NumPy Array:")
print(arr)


print("\n4b. Basic Operations:")

print("Addition:", arr + 5)
print("Subtraction:", arr - 5)
print("Multiplication:", arr * 2)
print("Division:", arr / 2)


arr10 = np.array([89, 85, 91, 107, 119, 108, 155, 169, 82, 124])

print("\n4c. Array with 10 Elements:")
print(arr10)

print("Elements from 1st to 5th:")
print(arr10[0:5])



names = np.array(["Mango", "Apple", "Orange", "Banana"])

print("\n4d. Original Array:")
print(names)

print("Array Sorted Alphabetically:")
print(np.sort(names))


numbers = np.array([89, 85, 91, 107, 119])

max_value = np.max(numbers)
filter_array = numbers[numbers == max_value]

print("\n4e. Original Array:")
print(numbers)

print("Maximum Value:", max_value)
print("Filter Array:", filter_array)
