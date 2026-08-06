import matplotlib.pyplot as plt

print("Shreyash Kadam S091")

categories = ["Data Structures", "Scala for DS", "Operating System", "Python for DS"]
scores = [65, 70, 74, 60]

plt.barh(categories, scores)

plt.title("Student Scores")
plt.xlabel("Scores")
plt.ylabel("Subjects")

plt.show()
