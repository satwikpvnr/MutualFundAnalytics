import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/08_investor_transactions.csv")

age_counts = df["age_group"].value_counts()

plt.figure(figsize=(8,5))
age_counts.plot(kind="bar")

plt.title("Investor Distribution by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Investors")
plt.grid(axis="y")

plt.tight_layout()
plt.savefig("reports/age_distribution.png")
plt.show()

print("Age distribution chart saved!")