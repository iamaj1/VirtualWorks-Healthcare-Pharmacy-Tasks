"""Task 2: Visualizations using synthetic healthcare-themed data."""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent
rng = np.random.default_rng(7)
n = 180
df = pd.DataFrame({"age": rng.integers(18, 90, n), "condition": rng.choice(["Hypertension", "Diabetes", "Asthma", "Cardiovascular"], n, p=[.36, .29, .17, .18]), "medication": rng.choice(["Medicine A", "Medicine B", "Medicine C", "Medicine D"], n)})
df["age_group"] = pd.cut(df["age"], [17, 29, 44, 59, 74, 100], labels=["18–29", "30–44", "45–59", "60–74", "75+"])
df.to_csv(OUT / "visualization_summary_data.csv", index=False)
charts = [("condition", "Synthetic Records by Condition", "condition_distribution.png", "Condition"), ("age_group", "Synthetic Records by Age Group", "age_group_distribution.png", "Age group"), ("medication", "Synthetic Records by Medication", "medication_counts.png", "Medication")]
for column, title, filename, xlabel in charts:
    counts = df[column].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(8, 5))
    counts.plot(kind="bar", ax=ax)
    ax.set_title(title); ax.set_xlabel(xlabel); ax.set_ylabel("Illustrative record count")
    ax.tick_params(axis="x", rotation=25); fig.tight_layout(); fig.savefig(OUT / filename, dpi=160); plt.close(fig)
print("Created summary CSV and three PNG charts.")
print(df.describe(include="all").to_string())
