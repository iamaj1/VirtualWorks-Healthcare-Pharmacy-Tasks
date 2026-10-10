# ADR / Pharmacovigilance Internship — Project Pack

This folder contains training/demo materials for the VirtualWorks dashboard tasks. Cases and data are entirely fictional and are provided for learning only.

## Task folders
1. [ADR Identification Basics](task1-adr-identification/)
2. [ADR Reporting & Documentation](task2-adr-reporting/)
3. [Causality Assessment](task3-causality-assessment/)
4. [Severity & Case Classification](task4-severity-classification/)
5. [Individual Case Safety Report (ICSR)](task5-icsr/)

## Setup
Install Python 3.10+ and dependencies from the repository-root `requirements.txt`:
```bash
pip install -r ../requirements.txt
```
Run each Python script from the task folder, e.g. `python report_validator.py`.

## Important limitations
These scripts are educational triage aids. They do not replace a qualified pharmacovigilance professional, company SOPs, local regulations, MedDRA coding review, clinical judgment, or validated safety databases. Never insert real patient identifiers or confidential reports into this public repository.