import pandas as pd
from sqlalchemy import create_engine

print("Creating database...")

engine = create_engine("sqlite:///bluestock_mf.db")

# Load cleaned files
nav = pd.read_csv("data/processed/clean_nav.csv")
transactions = pd.read_csv("data/processed/clean_transactions.csv")
performance = pd.read_csv("data/processed/clean_performance.csv")

# Load to SQLite
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)
performance.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("Database created successfully!")