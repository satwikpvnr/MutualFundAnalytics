import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/08_investor_transactions.csv")

age_amount = df.groupby("age_group")["amount_inr"].mean()

plt.figure(figsize=(8,5))
age_amount.plot(kind="bar")

plt.title("Average Investment Amount by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Average Amount (₹)")
plt.grid(axis="y")

plt.tight_layout()
plt.savefig("reports/age_amount.png")
plt.show()

print("Age amount chart saved!")