"""Task 3: Pharmacy sales analysis based on synthetic transactions."""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent
rng = np.random.default_rng(11)
products = ["Medicine A", "Medicine B", "Medicine C", "Medicine D", "Medicine E", "Medicine F"]
rows = []
for month in pd.date_range("2026-01-01", periods=6, freq="MS"):
    for product in products:
        units = int(rng.integers(20, 180))
        price = round(float(rng.uniform(35, 450)), 2)
        generic = product in ["Medicine B", "Medicine D", "Medicine F"]
        rows.append({
            "month": month.strftime("%Y-%m"), "product": product,
            "type": "Generic" if generic else "Brand", "units_sold": units,
            "unit_price": price, "revenue": round(units * price, 2),
        })
df = pd.DataFrame(rows)
df.to_csv(OUT / "synthetic_pharmacy_sales.csv", index=False)
top = df.groupby("product").agg(units_sold=("units_sold", "sum"), revenue=("revenue", "sum")).sort_values("revenue", ascending=False)
monthly = df.groupby("month")["revenue"].sum()
fig, ax = plt.subplots(figsize=(8, 5))
top["revenue"].sort_values().plot(kind="barh", ax=ax)
ax.set_title("Synthetic Revenue by Product")
ax.set_xlabel("Revenue (illustrative currency units)")
fig.tight_layout(); fig.savefig(OUT / "top_products_revenue.png", dpi=160); plt.close(fig)
fig, ax = plt.subplots(figsize=(8, 5))
monthly.plot(marker="o", ax=ax)
ax.set_title("Synthetic Monthly Pharmacy Revenue")
ax.set_ylabel("Revenue (illustrative currency units)")
fig.tight_layout(); fig.savefig(OUT / "monthly_revenue.png", dpi=160); plt.close(fig)
print("TOP PRODUCTS\n", top.to_string())
print("\nMONTHLY REVENUE\n", monthly.to_string())
print("\nBRAND VS GENERIC\n", df.groupby("type").agg(units=("units_sold", "sum"), revenue=("revenue", "sum")).to_string())
