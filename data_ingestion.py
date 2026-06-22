import pandas as pd
import os

folder = "data/raw"

for file in os.listdir(folder):

    if file.endswith(".csv"):

        print("\n" + "="*60)
        print("FILE:", file)
        print("="*60)

        df = pd.read_csv(os.path.join(folder, file))

        df["date"] = pd.to_datetime(
            df["date"],
            format="%d-%m-%Y"
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