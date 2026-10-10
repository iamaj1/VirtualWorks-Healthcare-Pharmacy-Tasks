"""Validate the fictional ADR intake CSV for training purposes."""
from pathlib import Path
import pandas as pd

HERE = Path(__file__).resolve().parent
INPUT = HERE / "sample_adr_report.csv"
OUTPUT = HERE / "validation_summary.txt"
REQUIRED = ["case_id", "patient_reference", "reporter_reference", "suspect_product", "reaction_event"]

def main():
    df = pd.read_csv(INPUT, dtype=str).fillna("")
    lines = ["EDUCATIONAL ADR INTAKE VALIDATION — NOT A REGULATORY DATABASE"]
    for idx, row in df.iterrows():
        missing = [col for col in REQUIRED if not row.get(col, "").strip()]
        lines.append(f"Case: {row.get('case_id', f'row-{idx + 1}')}")
        lines.append("Minimum information check: " + ("PASS" if not missing else "INCOMPLETE"))
        if missing:
            lines.append("Missing required fields: " + ", ".join(missing))
        follow_up = row.get("follow_up_needed", "").strip()
        lines.append("Follow-up noted: " + ("Yes" if follow_up and follow_up.lower() not in {"none", "no"} else "No"))
        lines.append("Causality: not automatically determined by this validator.")
        lines.append("")
    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))

if __name__ == "__main__":
    main()
