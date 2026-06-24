import pandas as pd
import numpy as np
from scipy.stats import linregress

print("Loading data...")

# Fund returns
fund_df = pd.read_csv("data/processed/returns_computed.csv")

# Benchmark data
bench_df = pd.read_csv("data/raw/10_benchmark_indices.csv")

# NIFTY100 only
bench_df = bench_df[bench_df["index_name"] == "NIFTY100"].copy()

bench_df["date"] = pd.to_datetime(bench_df["date"])
bench_df = bench_df.sort_values("date")

# Benchmark returns
bench_df["benchmark_return"] = bench_df["close_value"].pct_change()

results = []

for amfi_code, group in fund_df.groupby("amfi_code"):

    group["date"] = pd.to_datetime(group["date"])

    merged = pd.merge(
        group,
        bench_df[["date", "benchmark_return"]],
        on="date",
        how="inner"
    )

    merged = merged.dropna(
        subset=["daily_return", "benchmark_return"]
    )

    if len(merged) < 30:
        continue

    slope, intercept, r, p, stderr = linregress(
        merged["benchmark_return"],
        merged["daily_return"]
    )

    beta = slope

    alpha = intercept * 252 * 100

    results.append([
        amfi_code,
        round(alpha, 2),
        round(beta, 3),
        round(r**2, 3)
    ])

alpha_beta_df = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "alpha_pct",
        "beta",
        "r_squared"
    ]
)

alpha_beta_df.to_csv(
    "data/processed/alpha_beta.csv",
    index=False
)

print("\nTop Alpha Funds")
print(
    alpha_beta_df.sort_values(
        "alpha_pct",
        ascending=False
    ).head(10)
)

print("\nSaved successfully!")