import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Pivot for plotting
pivot_df = df.pivot(index="date", columns="fund_house", values="aum_lakh_crore")

# Plot
plt.figure(figsize=(12,6))

for col in pivot_df.columns:
    plt.plot(pivot_df.index, pivot_df[col], label=col)

plt.title("AUM Growth by Fund House")
plt.xlabel("Date")
plt.ylabel("AUM (Lakh Crore)")
plt.legend()
plt.grid(True)

# Save chart
plt.savefig("reports/aum_growth.png")
plt.show()

print("Chart saved successfully!")