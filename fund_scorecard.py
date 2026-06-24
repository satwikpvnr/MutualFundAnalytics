import pandas as pd

print("Loading files...")

cagr = pd.read_csv("data/processed/cagr_report.csv")
sharpe = pd.read_csv("data/processed/sharpe_values.csv")
alpha = pd.read_csv("data/processed/alpha_beta.csv")
maxdd = pd.read_csv("data/processed/max_drawdown.csv")

df = cagr.merge(sharpe, on="amfi_code")
df = df.merge(alpha, on="amfi_code")
df = df.merge(maxdd, on="amfi_code")

# Ranking metrics
df["cagr_rank"] = df["cagr_pct"].rank(ascending=False)
df["sharpe_rank"] = df["sharpe_ratio"].rank(ascending=False)
df["alpha_rank"] = df["alpha_pct"].rank(ascending=False)

# Smaller drawdown is better
df["drawdown_rank"] = df["max_drawdown_pct"].rank(ascending=False)

# Composite score
df["fund_score"] = (
    df["cagr_rank"] * 0.35 +
    df["sharpe_rank"] * 0.35 +
    df["alpha_rank"] * 0.20 +
    df["drawdown_rank"] * 0.10
)

scorecard = df.sort_values("fund_score")

scorecard.to_csv(
    "data/processed/fund_scorecard.csv",
    index=False
)

print("\nTop 10 Funds")
print(
    scorecard[
        [
            "amfi_code",
            "cagr_pct",
            "sharpe_ratio",
            "alpha_pct",
            "max_drawdown_pct",
            "fund_score"
        ]
    ].head(10)
)

print("\nSaved successfully!")