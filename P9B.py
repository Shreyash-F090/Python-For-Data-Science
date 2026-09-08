import pandas as pd

print("Shreyash Kadam S091")

df = pd.read_csv("songs.csv")

print("Song Dataset:")
print(df)

print("\nFirst 10 Records:")
print(df.head(10))

print("\nNumber of Songs:")
print(len(df))

print("\nColumn Names:")
print(df.columns)

print("\nAverage Rating:")
print(df["Rating"].mean())

print("\nAverage Streams:")
print(df["Streams"].mean())
