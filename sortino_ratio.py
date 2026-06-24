import pandas as pd
import numpy as np

print("Loading returns data...")

df = pd.read_csv("data/processed/returns_computed.csv")

risk_free_rate = 0.065

results = []

for amfi_code, group in df.groupby("amfi_code"):

    returns = group["daily_return"].dropna()

    if len(returns) == 0:
        continue

    annual_return = returns.mean() * 252

    downside_returns = returns[returns < 0]

    if len(downside_returns) == 0:
        continue

    downside_std = downside_returns.std() * np.sqrt(252)

    sortino = (
        (annual_return - risk_free_rate)
        / downside_std
    )

    results.append([
        amfi_code,
        round(annual_return * 100, 2),
        round(downside_std * 100, 2),
        round(sortino, 3)
    ])

sortino_df = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "annual_return_pct",
        "downside_risk_pct",
        "sortino_ratio"
    ]
)

sortino_df.to_csv(
    "data/processed/sortino_values.csv",
    index=False
)

print("\nTop Sortino Ratios")
print(
    sortino_df.sort_values(
        "sortino_ratio",
        ascending=False
    ).head(10)
)

print("\nSaved successfully!")