import pandas as pd

print("Shreyash Kadam S091")

# -----------------------------
# 5a. Create a DataFrame
# -----------------------------
print("\n5a. DataFrame Object")

data = {
    "Name": ["Amit", "Neha", "Rohan", "Priya"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 90, 88, 95]
}

df = pd.DataFrame(data)

print(df)

# -----------------------------
# 5b. Statistical Information
# -----------------------------
print("\n5b. Statistical Information")

print(df.describe())

# -----------------------------
# 5c. Create Pandas Series from Dictionary
# -----------------------------
print("\n5c. Pandas Series from Dictionary")

student = {
    "Amit": 85,
    "Neha": 90,
    "Rohan": 88,
    "Priya": 95
}

series = pd.Series(student)

print(series)

# -----------------------------
# 5d. Filter Series using Boolean Array
# -----------------------------
print("\n5d. Filtered Series (Marks >= 90)")

filtered = series[series >= 90]

print(filtered)
