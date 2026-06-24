import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/raw/05_category_inflows.csv")

# Convert month
df["month"] = pd.to_datetime(df["month"])

# Create pivot table
heatmap_data = df.pivot(
    index="category",
    columns="month",
    values="net_inflow_crore"
)

# Plot
plt.figure(figsize=(14,8))
sns.heatmap(
    heatmap_data,
    cmap="YlGnBu",
    annot=False
)

plt.title("Category-wise Net Inflow Heatmap")
plt.xlabel("Month")
plt.ylabel("Category")

plt.tight_layout()

plt.savefig("reports/category_heatmap.png")
plt.show()

print("Heatmap saved successfully!")