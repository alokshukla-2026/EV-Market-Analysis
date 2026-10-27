import pandas as pd

df = pd.read_csv("ev_data_cleaned.csv")
print("Cleaned dataset shape:", df.shape)
print("\nDuplicate rows:", df.duplicated().sum())
print("\nMissing values:")
print(df.isna().sum())
