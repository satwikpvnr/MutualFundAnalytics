import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Top 10 states
top_states = df["state"].value_counts().head(10)

plt.figure(figsize=(10,6))
top_states.plot(kind="barh")

plt.title("Top 10 States by Investor Transactions")
plt.xlabel("Number of Transactions")
plt.ylabel("State")

plt.tight_layout()
plt.savefig("reports/geo_distribution.png")
plt.show()

print("Geographic distribution chart saved!")