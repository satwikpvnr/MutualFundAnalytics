import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

# Convert month column
df["month"] = pd.to_datetime(df["month"])

# Plot SIP inflow trend
plt.figure(figsize=(12,6))
plt.plot(df["month"], df["sip_inflow_crore"], marker="o")

plt.title("Monthly SIP Inflow Trend (2022-2025)")
plt.xlabel("Month")
plt.ylabel("SIP Inflow (Crore ₹)")
plt.grid(True)

# Highlight Dec 2025 milestone
dec2025 = df[df["month"] == "2025-12-01"]

if not dec2025.empty:
    value = dec2025["sip_inflow_crore"].iloc[0]
    plt.scatter(dec2025["month"], value, s=100)
    plt.annotate(
        f"₹{value:,.0f} Cr",
        (dec2025["month"].iloc[0], value),
        xytext=(10,10),
        textcoords="offset points"
    )

plt.savefig("reports/sip_inflow_trend.png")
plt.show()

print("SIP Trend chart saved successfully!")