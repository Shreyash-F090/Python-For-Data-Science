import pandas as pd

data = {
    "Song_Name": [
        "Midnight Drive", "Golden Hour", "Ocean Eyes",
        "Afterglow", "Lost Stars", "Electric Heart",
        "Moonlight", "Dreamscape"
    ],
    "Genre": [
        "Pop", "Indie", "Pop", "Rock",
        "Indie", "EDM", "Romantic", "Pop"
    ],
    "Rating": [
        8.4, None, 8.7, 7.9,
        None, 9.3, 8.1, None
    ],
    "Streams": [
        1850000, 2640000, None, 1480000,
        980000, None, 1750000, 3890000
    ]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

print("\nMissing Values:")
print(df.isnull())

print("\nCount of Missing Values:")
print(df.isnull().sum())

df["Rating"] = df["Rating"].fillna(df["Rating"].mean())

df["Streams"] = df["Streams"].fillna(df["Streams"].mean())

print("\nCleaned Dataset:")
print(df)
