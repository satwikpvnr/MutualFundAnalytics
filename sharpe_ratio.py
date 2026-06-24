import pandas as pd
import numpy as np

print("Loading returns data...")

df = pd.read_csv("data/processed/returns_computed.csv")

risk_free_rate = 0.065  # 6.5%

results = []

for amfi_code, group in df.groupby("amfi_code"):

    returns = group["daily_return"].dropna()

    if len(returns) == 0:
        continue

    annual_return = returns.mean() * 252
    annual_volatility = returns.std() * np.sqrt(252)

    sharpe = (
        (annual_return - risk_free_rate)
        / annual_volatility
    )

    results.append([
        amfi_code,
        round(annual_return * 100, 2),
        round(annual_volatility * 100, 2),
        round(sharpe, 3)
    ])

sharpe_df = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "annual_return_pct",
        "annual_volatility_pct",
        "sharpe_ratio"
    ]
)

sharpe_df.to_csv(
    "data/processed/sharpe_values.csv",
    index=False
)

print("\nTop Sharpe Ratios")
print(
    sharpe_df.sort_values(
        "sharpe_ratio",
        ascending=False
    ).head(10)
)

print("\nSaved successfully!")