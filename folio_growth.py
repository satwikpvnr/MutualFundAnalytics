import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/06_industry_folio_count.csv")

df["month"] = pd.to_datetime(df["month"])

plt.figure(figsize=(12,6))

plt.plot(
    df["month"],
    df["total_folios_crore"],
    marker="o"
)

plt.title("Industry Folio Growth (2022-2026)")
plt.xlabel("Month")
plt.ylabel("Total Folios (Crore)")
plt.grid(True)

plt.tight_layout()

plt.savefig("reports/folio_growth.png")
plt.show()