"""Educational seriousness/severity classification from fictional cases."""
from pathlib import Path
import pandas as pd

HERE = Path(__file__).resolve().parent
INPUT = HERE / "sample_cases.csv"
OUTPUT = HERE / "severity_classification_results.csv"
SERIOUSNESS_FIELDS = [
    "death", "life_threatening", "hospitalization", "significant_disability",
    "congenital_anomaly", "other_medically_important",
]
YES = {"yes", "y", "true", "1"}

def classify(row):
    flags = [field for field in SERIOUSNESS_FIELDS if str(row.get(field, "")).strip().lower() in YES]
    seriousness = "Serious criterion reported" if flags else "No listed serious criterion marked"
    return pd.Series({
        "seriousness_classification": seriousness,
        "criteria_flagged": "; ".join(flags) if flags else "None marked",
        "review_note": "Confirm against source documents and applicable SOP; this script does not make a clinical judgment.",
    })

def main():
    df = pd.read_csv(INPUT, dtype=str).fillna("")
    result = pd.concat([df, df.apply(classify, axis=1)], axis=1)
    result.to_csv(OUTPUT, index=False)
    print(result[["case_id", "severity_intensity", "seriousness_classification", "criteria_flagged"]].to_string(index=False))
    print(f"\nSaved: {OUTPUT.name}")

if __name__ == "__main__":
    main()
