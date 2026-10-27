import pandas as pd

df = pd.read_csv("ev_data_cleaned.csv")
lines = []
lines.append("ELECTRIC VEHICLE MARKET ANALYSIS - INSIGHTS")
lines.append("Author: Alok Shukla")
lines.append(f"Total records: {len(df)}")

if "battery_capacity_kWh" in df.columns:
    lines.append(f"Average battery capacity (kWh): {df['battery_capacity_kWh'].mean():.2f}")
if "range_km" in df.columns:
    lines.append(f"Average driving range (km): {df['range_km'].mean():.2f}")
    lines.append(f"Maximum driving range (km): {df['range_km'].max():.2f}")
if "efficiency_wh_per_km" in df.columns:
    lines.append(f"Average efficiency (Wh/km): {df['efficiency_wh_per_km'].mean():.2f}")
if {"battery_capacity_kWh","range_km"}.issubset(df.columns):
    lines.append(f"Battery-range correlation: {df['battery_capacity_kWh'].corr(df['range_km']):.2f}")
if "car_body_type" in df.columns:
    lines.append("Most represented body type: " + str(df["car_body_type"].mode().iloc[0]))

with open("ev_insights_report.txt","w",encoding="utf-8") as f:
    f.write("\n".join(lines))

print("\n".join(lines))
