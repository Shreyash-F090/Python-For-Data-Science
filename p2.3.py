numbers = [90, 122, 88, 84, 129]
largest = max(numbers)
print("Largest number:", largest)

duplicate_list = [90, 122, 90, 84, 88, 84, 90, 90]
unique_list = list(set(duplicate_list))
print("List after removing duplicates:", unique_list)


num_list = [90, 122, 88, 84, 129, 127, 74]
even_count = 0

for num in num_list:
    if num % 2 == 0:
        even_count += 1

print("Number of even elements:", even_count)

user_list = []

print("\nEnter 5 numbers:")
for i in range(5):
    num = int(input(f"Number {i+1}: "))
    user_list.append(num)

print("List entered by user:", user_list)

def calculate_average(lst):
    return sum(lst) / len(lst)

average = calculate_average(user_list)
print("Average of the list:", average)

text = "Shreyash"
char_list = list(text)
print("List of characters:", char_list)

words = ["Shreyash", "Kadam", "MVLU", "S090", ""]
sentence = " ".join(words)
print("Joined String:", sentence)
