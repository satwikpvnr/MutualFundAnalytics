import pandas as pd

print("Loading nav_history...")

df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

# Convert date column
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Sort data
df = df.sort_values(by=["amfi_code", "date"])

# Forward fill NAV values within each fund
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Remove duplicates
df = df.drop_duplicates()

# Keep only valid NAV values
df = df[df["nav"] > 0]

print("Cleaned Shape:", df.shape)

# Save cleaned file
df.to_csv("data/processed/clean_nav.csv", index=False)

print("Saved successfully!")