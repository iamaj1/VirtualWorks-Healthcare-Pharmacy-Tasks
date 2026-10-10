# Task 5 — Individual Case Safety Report (ICSR)

## Objective
Generate a structured fictional ICSR training report with case identifiers, reporter/patient references, suspect product, event, chronology, outcome, seriousness criteria, causality rationale, and follow-up needs.

## Run
```bash
python generate_icsr.py
```

## Outputs
- `sample_icsr.json`
- `sample_icsr_narrative.md`
- `icsr_validation.txt`

The script checks the common minimum screening elements used to determine whether a safety report contains a patient reference, reporter, suspect product, and reported reaction. This is not a validated E2B(R3) file, regulatory submission, or safety-database export. Real ICSRs must be processed with the proper validated system and reporting timelines.