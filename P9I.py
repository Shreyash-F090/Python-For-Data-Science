import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("songs.csv")

plt.figure(figsize=(10, 5))
plt.bar(df["Song_Name"], df["Rating"])
plt.xlabel("Song Name")
plt.ylabel("Rating")
plt.title("Song Ratings")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(df["Song_Name"], df["Rating"], marker="o")
plt.xlabel("Song Name")
plt.ylabel("Rating")
plt.title("Song Ratings - Line Chart")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df["Rating"], bins=5)
plt.xlabel("Rating")
plt.ylabel("Number of Songs")
plt.title("Distribution of Song Ratings")
plt.show()

genre_count = df["Genre"].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(
    genre_count,
    labels=genre_count.index,
    autopct="%1.1f%%"
)
plt.title("Songs by Genre")
plt.show()
