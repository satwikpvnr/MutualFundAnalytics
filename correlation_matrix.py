import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load NAV history
df = pd.read_csv("data/raw/02_nav_history.csv")

df["date"] = pd.to_datetime(df["date"])

# Select 10 funds
funds = df["amfi_code"].unique()[:10]

df = df[df["amfi_code"].isin(funds)]

# Pivot table
pivot_df = df.pivot(
    index="date",
    columns="amfi_code",
    values="nav"
)

# Daily returns
returns = pivot_df.pct_change().dropna()

# Correlation matrix
corr_matrix = returns.corr()

plt.figure(figsize=(10,8))

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("NAV Return Correlation Matrix")

plt.tight_layout()

plt.savefig("reports/correlation_matrix.png")

plt.show()