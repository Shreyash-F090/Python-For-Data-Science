import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

print(tips.head())

sns.scatterplot(x="total_bill", y="tip", data=tips)

plt.title("S091 Shreyash Kadam")
plt.xlabel("Total Bill")
plt.ylabel("Tip")

plt.show(block=True)
