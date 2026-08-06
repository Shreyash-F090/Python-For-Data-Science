import matplotlib.pyplot as plt
import numpy as np

print("Om Wala S119")

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

data = np.random.normal(0, 1, 100)

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(x, y, color="blue", marker="o", linewidth=2)
plt.title("Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.hist(data, bins=15, color="orange", edgecolor="black")
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)

plt.tight_layout()
plt.show()
