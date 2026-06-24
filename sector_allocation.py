import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/09_portfolio_holdings.csv")

# Group by sector
sector_weights = df.groupby("sector")["weight_pct"].sum()

# Top 10 sectors
sector_weights = sector_weights.sort_values(ascending=False).head(10)

plt.figure(figsize=(8,8))

plt.pie(
    sector_weights,
    labels=sector_weights.index,
    autopct="%1.1f%%"
)

plt.title("Portfolio Sector Allocation")

plt.tight_layout()

plt.savefig("reports/sector_allocation.png")

plt.show()