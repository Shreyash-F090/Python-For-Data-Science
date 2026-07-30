import pandas as pd

print("Shreyash Kadam S091")


df = pd.read_csv("stocks.csv")

print("\n5a. DataFrame:")
print(df.head())


print("\n5b. Statistical Information:")
print(df.describe())


series = pd.Series(df["AMZN"])

print("\n5c. Pandas Series (AMZN):")
print(series.head(10))


filtered = series[series > 500]

print("\n5d. AMZN Prices Greater Than 500:")
print(filtered)
