import pandas as pd
import numpy as np

print("Loading NAV data...")

df = pd.read_csv("data/processed/clean_nav.csv")

df["date"] = pd.to_datetime(df["date"])

results = []

for amfi_code, group in df.groupby("amfi_code"):

    group = group.sort_values("date")

    start_nav = group["nav"].iloc[0]
    end_nav = group["nav"].iloc[-1]

    years = (group["date"].max() - group["date"].min()).days / 365

    cagr = ((end_nav / start_nav) ** (1 / years) - 1) * 100

    results.append([
        amfi_code,
        round(start_nav, 2),
        round(end_nav, 2),
        round(years, 2),
        round(cagr, 2)
    ])

cagr_df = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "start_nav",
        "end_nav",
        "years",
        "cagr_pct"
    ]
)

cagr_df.to_csv(
    "data/processed/cagr_report.csv",
    index=False
)

print("\nTop 10 CAGR Funds")
print(
    cagr_df.sort_values(
        "cagr_pct",
        ascending=False
    ).head(10)
)

print("\nSaved successfully!")