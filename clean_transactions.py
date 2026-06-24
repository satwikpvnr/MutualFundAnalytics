import pandas as pd

print("Loading investor transactions...")

df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

# Convert date
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .astype(str)
    .str.strip()
    .str.title()
)

# Keep valid transaction types only
valid_types = ["Sip", "Lumpsum", "Redemption"]

df = df[df["transaction_type"].isin(valid_types)]

# Amount must be greater than zero
df = df[df["amount_inr"] > 0]

# Standardize KYC values
df["kyc_status"] = (
    df["kyc_status"]
    .astype(str)
    .str.strip()
    .str.title()
)

valid_kyc = ["Verified", "Pending"]

df = df[df["kyc_status"].isin(valid_kyc)]

# Remove duplicates
df = df.drop_duplicates()

print("Cleaned Shape:", df.shape)

print("\nTransaction Types:")
print(df["transaction_type"].value_counts())

print("\nKYC Status:")
print(df["kyc_status"].value_counts())

# Save file
df.to_csv(
    "data/processed/clean_transactions.csv",
    index=False
)

print("\nSaved successfully!")