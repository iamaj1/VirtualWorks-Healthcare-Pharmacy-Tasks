# Task 2 — ADR Reporting & Documentation

## Objective
Complete a structured report from a fictional case, check minimum case information, and document follow-up items.

## Files
- `case_scenario.md`: fictional case narrative
- `sample_adr_report.csv`: structured sample report
- `report_validator.py`: checks required reporting fields and writes a validation summary

## Run
```bash
python report_validator.py
```

The script checks for an identifiable patient reference, reporter, suspect product, and reaction/event—the minimum screening elements commonly used to assess whether a report can be processed. Additional fields help support follow-up and medical review.

## Important
This is an educational example, not a validated regulatory submission form. Use the applicable safety database, company SOP, local reporting rules, and approved terminology in real work. The sample contains no real patient identifiers.