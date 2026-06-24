import pandas as pd
import matplotlib.pyplot as plt

print("Loading NAV data...")

df = pd.read_csv("data/raw/02_nav_history.csv")

df["date"] = pd.to_datetime(df["date"])

# Select top 5 funds for visualization
top_funds = df["amfi_code"].unique()[:5]

plt.figure(figsize=(12,6))

for fund in top_funds:
    temp = df[df["amfi_code"] == fund]
    plt.plot(temp["date"], temp["nav"], label=str(fund))

plt.title("NAV Trend Analysis")
plt.xlabel("Date")
plt.ylabel("NAV")
plt.legend()
plt.grid()

plt.savefig("reports/nav_trend.png")
plt.show()

print("Chart saved successfully!")