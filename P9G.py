import pandas as pd

print("Shreyash Kadam S091")

df = pd.read_csv("songs.csv")

print("Average Rating:", df["Rating"].mean())

print("Maximum Rating:", df["Rating"].max())

print("Minimum Rating:", df["Rating"].min())

print("Median Rating:", df["Rating"].median())

print("Standard Deviation:", df["Rating"].std())

print("Average Streams:", df["Streams"].mean())

print("Number of Songs:", df["Song_Name"].count())

print("Songs with Rating Above 8.5:",
      (df["Rating"] > 8.5).sum())
