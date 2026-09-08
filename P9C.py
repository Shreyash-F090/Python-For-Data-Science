import pandas as pd

print("Shreyash Kadam S091")

df = pd.read_csv("songs.csv")

print("Song Name and Rating:")
print(df[["Song_Name", "Rating"]])

print("\nSongs with Rating Greater Than 8.5:")
print(df[df["Rating"] > 8.5])

print("\nSongs with More Than 3,000,000 Streams:")
print(df[df["Streams"] > 3000000])

print("\nPop Songs:")
print(df[df["Genre"] == "Pop"])

print("\nHindi Songs:")
print(df[df["Language"] == "Hindi"])

print("\nSongs with Rating Greater Than 8.5 and Streams Above 3,000,000:")
print(df[(df["Rating"] > 8.5) & (df["Streams"] > 3000000)])
