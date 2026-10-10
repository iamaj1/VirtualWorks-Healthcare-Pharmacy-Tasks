"""Educational causality triage using simplified WHO-UMC-style considerations.
This is not an official WHO algorithm or clinical conclusion.
"""
from pathlib import Path
import pandas as pd

HERE = Path(__file__).resolve().parent
INPUT = HERE / "sample_cases.csv"
OUTPUT = HERE / "causality_assessment_results.csv"

def classify(row):
    timing = str(row["temporal_relationship"]).strip().lower()
    alternative = str(row["alternative_cause"]).strip().lower()
    dechallenge = str(row["dechallenge"]).strip().lower()
    rechallenge = str(row["rechallenge"]).strip().lower()
    objective = str(row["objective_evidence"]).strip().lower()

    if timing == "reasonable" and alternative == "unlikely" and dechallenge == "positive" and rechallenge == "positive" and objective == "yes":
        return "Certain (training example)"
    if timing == "reasonable" and alternative == "unlikely" and dechallenge == "positive" and rechallenge in {"not_done", "unknown", "negative"}:
        return "Probable/Likely (training example)"
    if timing == "reasonable" and alternative in {"possible", "likely", "unknown"}:
        return "Possible (training example)"
    if timing == "reasonable" and dechallenge == "unknown" and alternative != "unlikely":
        return "Possible (training example)"
    return "Unassessable / needs more information"

def main():
    df = pd.read_csv(INPUT, dtype=str).fillna("")
    df["educational_category"] = df.apply(classify, axis=1)
    df["review_note"] = "Human PV review required; timing alone does not establish causality."
    df.to_csv(OUTPUT, index=False)
    print(df[["case_id", "educational_category", "review_note"]].to_string(index=False))
    print(f"\nSaved: {OUTPUT.name}")

if __name__ == "__main__":
    main()
