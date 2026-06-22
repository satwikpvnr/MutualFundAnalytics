import pandas as pd
import os

folder = "data/raw"

for file in os.listdir(folder):

    if file.endswith(".csv"):

        print("\n" + "="*60)
        print("FILE:", file)
        print("="*60)

        df = pd.read_csv(os.path.join(folder, file))

        if "date" in df.columns:
            df["date"] = pd.to_datetime(
                df["date"],
                format="%d-%m-%Y",
                errors="coerce"
            )
        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\n" + "="*60)
print("FUND MASTER ANALYSIS")
print("="*60)

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("\nNumber of Fund Houses:")
print(fund_master["fund_house"].nunique())

print("\nFund Houses:")
print(fund_master["fund_house"].unique())

print("\nCategories:")
print(fund_master["category"].unique())

print("\nSub Categories:")
print(fund_master["sub_category"].unique())

print("\nRisk Categories:")
print(fund_master["risk_category"].unique())


print("\n" + "="*60)
print("AMFI CODE VALIDATION")
print("="*60)

nav_history = pd.read_csv("data/raw/02_nav_history.csv")

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes

print("Fund Master Codes :", len(fund_codes))
print("NAV History Codes :", len(nav_codes))

if len(missing_codes) == 0:
    print("\nPASS: All AMFI codes exist in NAV history")
else:
    print("\nFAIL: Missing Codes Found")
    print(missing_codes)