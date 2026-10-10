"""Task 1: Healthcare data cleaning demo. Uses synthetic records only."""
from pathlib import Path
import numpy as np
import pandas as pd

OUT = Path(__file__).resolve().parent
rng = np.random.default_rng(42)
df = pd.DataFrame({
    "Patient_ID": [f"S{i:03d}" for i in range(1, 31)],
    "Age": rng.integers(18, 86, 30).astype(float),
    "Gender": rng.choice(["Female", "Male", " female ", "Male", None], 30),
    "Condition": rng.choice(["Hypertension", "Diabetes", "Asthma", "Cardiovascular"], 30),
    "Medication": rng.choice(["Drug A", "Drug B", "Drug C", None], 30),
    "Length_of_Stay_Days": rng.integers(1, 15, 30).astype(float),
})
df.loc[[2, 8, 17], "Age"] = np.nan
df.loc[[4, 12], "Length_of_Stay_Days"] = np.nan
df = pd.concat([df, df.iloc[[0]]], ignore_index=True)
before_rows = len(df)
before_missing = int(df.isna().sum().sum())
before_duplicates = int(df.duplicated().sum())
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
df = df.drop_duplicates()
for col in ["gender", "condition", "medication"]:
    df[col] = df[col].astype("string").str.strip().str.title()
for col in ["age", "length_of_stay_days"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")
    df[col] = df[col].fillna(df[col].median())
for col in ["gender", "medication"]:
    mode = df[col].mode(dropna=True)
    df[col] = df[col].fillna(mode.iloc[0] if not mode.empty else "Unknown")
df.to_csv(OUT / "cleaned_healthcare_data.csv", index=False)
lines = ["SYNTHETIC DEMONSTRATION DATA — NOT REAL PATIENT RECORDS", f"Rows before cleaning: {before_rows}", f"Duplicate rows removed: {before_duplicates}", f"Missing cells before cleaning: {before_missing}", f"Rows after cleaning: {len(df)}", f"Missing cells after cleaning: {int(df.isna().sum().sum())}", "", "Numeric summary:", df[["age", "length_of_stay_days"]].describe().to_string(), "", "Records by condition:", df["condition"].value_counts().to_string()]
(OUT / "cleaning_summary.txt").write_text("\n".join(lines), encoding="utf-8")
print("\n".join(lines))
