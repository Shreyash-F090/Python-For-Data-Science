import matplotlib.pyplot as plt

print("Shreyash Kadam S091")

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, color="red", linestyle="--", marker="o")

plt.title("Simple Line Plot")
plt.xlabel("Numbers")
plt.ylabel("Doubles")

plt.show()
