import pandas as pd

print("Shreyash Kadam S091")

df = pd.read_csv("songs.csv")

print("Number of Songs in Each Genre:")
print(df.groupby("Genre")["Song_Name"].count())

print("\nAverage Rating by Genre:")
print(df.groupby("Genre")["Rating"].mean())

print("\nMaximum Rating by Genre:")
print(df.groupby("Genre")["Rating"].max())

print("\nAverage Streams by Genre:")
print(df.groupby("Genre")["Streams"].mean())
import pandas as pd

df = pd.read_csv("songs.csv")

print("Number of Songs in Each Genre:")
print(df.groupby("Genre")["Song_Name"].count())

print("\nAverage Rating by Genre:")
print(df.groupby("Genre")["Rating"].mean())

print("\nMaximum Rating by Genre:")
print(df.groupby("Genre")["Rating"].max())

print("\nAverage Streams by Genre:")
print(df.groupby("Genre")["Streams"].mean())
