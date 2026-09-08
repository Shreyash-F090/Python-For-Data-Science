import pandas as pd

print("Shreyash Kadam S091")

df = pd.read_csv("songs.csv")

df["Popularity"] = df["Streams"].apply(
    lambda x: "Highly Popular" if x >= 3000000 else "Popular" if x >= 2000000 else "Less Popular"
)

def calculate_rating_category(rating):
    if rating >= 9:
        return "Excellent"
    elif rating >= 8:
        return "Very Good"
    elif rating >= 7:
        return "Good"
    else:
        return "Average"

df["Rating_Category"] = df["Rating"].apply(calculate_rating_category)

print(df)
