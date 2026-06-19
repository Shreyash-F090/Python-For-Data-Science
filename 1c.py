for i in range(1, 11):
    print("Square of", i, "=", i * i)

count = 0

for i in range(5):
    num = int(input("Enter a number: "))
    
    if num % 2 == 0:
        count += 1

print("Number of even numbers =", count)
