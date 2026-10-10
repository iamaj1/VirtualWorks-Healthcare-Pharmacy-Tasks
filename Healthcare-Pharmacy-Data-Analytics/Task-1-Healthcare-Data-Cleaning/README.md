# Task 1 — Healthcare Data Cleaning & Understanding

## Objective
Demonstrate data profiling, missing-value review, duplicate identification/removal, standardized column/category naming, and descriptive summaries.

## Run
```bash
python analysis.py
```

## Generated outputs
- `cleaned_healthcare_data.csv`
- `cleaning_summary.txt`

## Methods and limits
The script makes synthetic data, reports quality issues before/after cleaning, drops exact duplicate rows, standardizes labels, imputes numeric missing values with column medians, and fills categorical missing values with the mode. These are demonstration choices; real clinical datasets need a data dictionary, documented rules, and domain review.
