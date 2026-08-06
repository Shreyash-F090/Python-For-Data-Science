import matplotlib.pyplot as plt
import numpy as np

print("Shreyash Kadam S091")

data = np.random.normal(size=100)

plt.hist(data, bins=20)

plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")


plt.grid()

plt.show()
