# Task 4 — Severity & Case Classification

## Objective
Classify the *intensity* of an event separately from regulatory *seriousness* and document which seriousness criteria are reported.

## Run
```bash
python classify_cases.py
```

The script produces an educational classification CSV. Severity (mild/moderate/severe) describes intensity; seriousness relates to outcomes/criteria such as death, life-threatening event, hospitalization/prolongation, significant disability, congenital anomaly, or another medically important event. They are not interchangeable.

## Limitations
This is a simple training aid, not a substitute for clinical evaluation, local regulations, or the company's pharmacovigilance SOP. Verify each criterion from source documents; do not infer seriousness from symptom intensity alone.