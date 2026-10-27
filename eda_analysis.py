import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv("ev_data_cleaned.csv")
os.makedirs("charts", exist_ok=True)

if "brand" in df.columns:
    df["brand"].value_counts().head(10).plot(kind="bar")
    plt.title("Top 10 EV Brands")
    plt.xlabel("Brand")
    plt.ylabel("Number of Records")
    plt.tight_layout()
    plt.savefig("charts/top_10_brands.png", dpi=200)
    plt.close()

if "range_km" in df.columns:
    df["range_km"].dropna().plot(kind="hist", bins=20)
    plt.title("EV Driving Range Distribution")
    plt.xlabel("Range (km)")
    plt.ylabel("Number of Records")
    plt.tight_layout()
    plt.savefig("charts/ev_range_distribution.png", dpi=200)
    plt.close()

if {"battery_capacity_kWh","range_km"}.issubset(df.columns):
    sns.scatterplot(data=df, x="battery_capacity_kWh", y="range_km")
    plt.title("Battery Capacity vs Driving Range")
    plt.xlabel("Battery Capacity (kWh)")
    plt.ylabel("Driving Range (km)")
    plt.tight_layout()
    plt.savefig("charts/battery_vs_range.png", dpi=200)
    plt.close()

if "car_body_type" in df.columns:
    df["car_body_type"].value_counts().plot(kind="bar")
    plt.title("EV Models by Body Type")
    plt.xlabel("Body Type")
    plt.ylabel("Number of Records")
    plt.tight_layout()
    plt.savefig("charts/ev_body_types.png", dpi=200)
    plt.close()

print("EDA charts created in the charts folder.")
