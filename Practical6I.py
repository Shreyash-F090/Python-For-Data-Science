import matplotlib.pyplot as plt
import numpy as np

print("Shreyash Kadam S091")

plt.subplot(2, 2, 1)
plt.plot([1, 2, 3, 4], [2, 4, 6, 8])
plt.title("Line Plot")

plt.subplot(2, 2, 2)
plt.bar(["A", "B", "C", "D"], [10, 20, 15, 25])
plt.title("Bar Chart")

plt.subplot(2, 2, 3)
plt.scatter([1, 2, 3, 4], [5, 7, 6, 8])
plt.title("Scatter Plot")

plt.subplot(2, 2, 4)
data = np.random.normal(size=100)
plt.hist(data)
plt.title("Histogram")

plt.show()
