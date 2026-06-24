import pandas as pd

print("Loading NAV data...")

df = pd.read_csv("data/processed/clean_nav.csv")

df["date"] = pd.to_datetime(df["date"])

df = df.sort_values(["amfi_code", "date"])

# Daily Return
df["daily_return"] = df.groupby("amfi_code")["nav"].pct_change()

# Annualized Return
df["annualized_return"] = (
    (1 + df["daily_return"]).pow(252) - 1
)

df.to_csv(
    "data/processed/returns_computed.csv",
    index=False
)

print("Saved successfully!")
print(df.head())