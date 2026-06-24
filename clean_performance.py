import pandas as pd

print("Loading scheme performance...")

df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Original Shape:", df.shape)

# Convert numeric columns
numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct",
    "morningstar_rating"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove rows with invalid returns
df = df.dropna(
    subset=[
        "return_1yr_pct",
        "return_3yr_pct",
        "return_5yr_pct"
    ]
)

# Expense ratio validation (0.1% - 2.5%)
invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nInvalid Expense Ratios:", len(invalid_expense))

# Sharpe ratio validation
invalid_sharpe = df[
    df["sharpe_ratio"].isna()
]

print("Invalid Sharpe Ratios:", len(invalid_sharpe))

# Remove duplicates
df = df.drop_duplicates()

print("Cleaned Shape:", df.shape)

# Save cleaned dataset
df.to_csv(
    "data/processed/clean_performance.csv",
    index=False
)

print("Saved successfully!")