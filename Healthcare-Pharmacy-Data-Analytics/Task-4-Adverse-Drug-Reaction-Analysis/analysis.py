"""Task 4: Synthetic ADR reporting analysis; not clinical evidence."""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent
rng = np.random.default_rng(21)
symptoms = ["Nausea", "Headache", "Dizziness", "Rash", "Fatigue", "Abdominal discomfort"]
medicines = ["Medicine A", "Medicine B", "Medicine C", "Medicine D"]
n = 140
df = pd.DataFrame({
    "report_id": [f"ADR{i:04d}" for i in range(1, n + 1)],
    "suspected_medicine": rng.choice(medicines, n),
    "symptom": rng.choice(symptoms, n, p=[.23, .19, .18, .12, .16, .12]),
    "seriousness": rng.choice(["Non-serious", "Serious"], n, p=[.84, .16]),
    "reported_age": rng.integers(18, 90, n),
})
df.to_csv(OUT / "synthetic_adr_reports.csv", index=False)
counts = df["symptom"].value_counts()
fig, ax = plt.subplots(figsize=(8, 5))
counts.sort_values().plot(kind="barh", ax=ax)
ax.set_title("Synthetic ADR Reports by Symptom"); ax.set_xlabel("Illustrative report count")
fig.tight_layout(); fig.savefig(OUT / "adr_symptom_frequency.png", dpi=160); plt.close(fig)
print("SYMPTOM FREQUENCY\n", counts.to_string())
print("\nMEDICINE × SYMPTOM COUNTS\n", pd.crosstab(df["suspected_medicine"], df["symptom"]).to_string())
share = df.groupby("suspected_medicine")["seriousness"].apply(lambda s: (s == "Serious").mean() * 100)
print("\nILLUSTRATIVE SERIOUS REPORT SHARE (%)\n", share.round(1).to_string())
print("\nSynthetic demonstration only: not a validated safety signal and does not establish causality.")
