import pandas as pd

input_file = "electric_vehicles_spec_2025.csv"
output_file = "ev_data_cleaned.csv"

df = pd.read_csv(input_file)
df.columns = [c.strip() for c in df.columns]

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].astype(str).str.strip()

if "model" in df.columns:
    df["model"] = df["model"].replace({"nan": "Unknown", "": "Unknown"})

df = df.drop_duplicates()
df.to_csv(output_file, index=False)

print(f"Cleaned dataset saved to {output_file}")
print("Rows:", len(df))
print("Columns:", len(df.columns))
