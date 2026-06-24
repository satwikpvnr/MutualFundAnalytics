import pandas as pd

print("Loading NAV data...")

df = pd.read_csv("data/processed/clean_nav.csv")

df["date"] = pd.to_datetime(df["date"])

results = []

for amfi_code, group in df.groupby("amfi_code"):

    group = group.sort_values("date")

    rolling_max = group["nav"].cummax()

    drawdown = (
        (group["nav"] - rolling_max)
        / rolling_max
    ) * 100

    max_dd = drawdown.min()

    results.append([
        amfi_code,
        round(max_dd, 2)
    ])

maxdd_df = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "max_drawdown_pct"
    ]
)

maxdd_df.to_csv(
    "data/processed/max_drawdown.csv",
    index=False
)

print("\nWorst Drawdowns")
print(
    maxdd_df.sort_values(
        "max_drawdown_pct"
    ).head(10)
)

print("\nSaved successfully!")