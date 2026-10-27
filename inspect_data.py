import pandas as pd
df = pd.read_csv("electric_vehicles_spec_2025.csv")
print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())
print("\nMissing values:")
print(df.isna().sum())
print("\nDuplicate rows:", df.duplicated().sum())
