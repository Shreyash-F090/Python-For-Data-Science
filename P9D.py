import pandas as pd

print("Shreyash Kadam S091")

df = pd.read_csv("songs.csv")

print("Rating in Ascending Order:")
print(df.sort_values("Rating"))

print("\nRating in Descending Order:")
print(df.sort_values("Rating", ascending=False))

print("\nStreams in Descending Order:")
print(df.sort_values("Streams", ascending=False))

print("\nTop 5 Songs:")
print(df.sort_values("Rating", ascending=False).head(5))

print("\nBottom 3 Songs:")
print(df.sort_values("Rating").head(3))
