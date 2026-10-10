"""Build a fictional ICSR training output from sample_case.json."""
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
INPUT = HERE / "sample_case.json"
JSON_OUT = HERE / "sample_icsr.json"
NARRATIVE_OUT = HERE / "sample_icsr_narrative.md"
VALIDATION_OUT = HERE / "icsr_validation.txt"

MINIMUM_FIELDS = [
    ("patient.patient_reference", "patient reference"),
    ("reporter.reporter_reference", "reporter reference"),
    ("suspect_product.product_name", "suspect product"),
    ("reaction.reported_term", "reported reaction/event"),
]

def nested_get(obj, dotted):
    current = obj
    for part in dotted.split("."):
        if not isinstance(current, dict):
            return None
        current = current.get(part)
    return current

def main():
    case = json.loads(INPUT.read_text(encoding="utf-8"))
    missing = [label for key, label in MINIMUM_FIELDS if not str(nested_get(case, key) or "").strip()]
    normalized = {
        "case_id": case.get("case_id"),
        "case_type": case.get("case_type", "Fictional training case"),
        "patient": case.get("patient", {}),
        "reporter": case.get("reporter", {}),
        "suspect_product": case.get("suspect_product", {}),
        "reaction": case.get("reaction", {}),
        "causality": case.get("causality", {}),
        "follow_up_questions": case.get("follow_up_questions", []),
        "disclaimer": case.get("disclaimer", "Fictional training example only; not for regulatory submission."),
    }
    JSON_OUT.write_text(json.dumps(normalized, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    patient = normalized["patient"]
    reporter = normalized["reporter"]
    product = normalized["suspect_product"]
    reaction = normalized["reaction"]
    causal = normalized["causality"]
    lines = [
        "# Individual Case Safety Report (ICSR) — Fictional Training Example",
        "",
        f"**Case ID:** {normalized.get('case_id', 'Not provided')}",
        f"**Case type:** {normalized.get('case_type', 'Fictional training case')}",
        "",
        "## Patient",
        f"- Reference: {patient.get('patient_reference', 'Not provided')}",
        f"- Age group: {patient.get('age_group', 'Not provided')}",
        f"- Sex: {patient.get('sex', 'Not provided')}",
        "",
        "## Reporter",
        f"- Reference: {reporter.get('reporter_reference', 'Not provided')}",
        f"- Qualification: {reporter.get('qualification', 'Not provided')}",
        f"- Contact details: {reporter.get('contact_details', 'Not provided')}",
        "",
        "## Suspect product",
        f"- Product: {product.get('product_name', 'Not provided')}",
        f"- Dose: {product.get('dose', 'Not provided')}",
        f"- Route: {product.get('route', 'Not provided')}",
        f"- Therapy start: {product.get('therapy_start_date', 'Not provided')}",
        f"- Therapy stop: {product.get('therapy_stop_date', 'Not provided')}",
        "",
        "## Reaction / event",
        f"- Reported term: {reaction.get('reported_term', 'Not provided')}",
        f"- Onset: {reaction.get('onset_date', 'Not provided')}",
        f"- Outcome: {reaction.get('outcome', 'Not provided')}",
        f"- Intensity: {reaction.get('severity_intensity', 'Not provided')}",
        f"- Seriousness information: {reaction.get('seriousness', 'Not provided')}",
        "",
        "## Causality information",
        f"- Educational assessment: {causal.get('educational_assessment', 'Not assessed')}",
        f"- Rationale: {causal.get('rationale', 'Not provided')}",
        f"- Final medical assessment: {causal.get('final_medical_assessment', 'Not performed')}",
        "",
        "## Follow-up needed",
    ]
    lines.extend([f"- {question}" for question in normalized["follow_up_questions"]] or ["- No follow-up question listed."])
    lines += [
        "",
        "## Minimum information screening",
        "Result: " + ("INCOMPLETE — " + ", ".join(missing) if missing else "The example contains the listed screening elements."),
        "",
        "> **Disclaimer:** This is fictional training content, not a validated E2B(R3) file, safety database export, medical assessment, or regulatory submission.",
    ]
    NARRATIVE_OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    validation = [
        "ICSR TRAINING OUTPUT — NOT FOR REGULATORY SUBMISSION",
        f"Case ID: {normalized.get('case_id', 'Not provided')}",
        "Minimum information check: " + ("INCOMPLETE" if missing else "SCREENING ELEMENTS PRESENT"),
        "Missing items: " + (", ".join(missing) if missing else "None of the configured screening fields"),
        f"Follow-up questions: {len(normalized['follow_up_questions'])}",
        "Human pharmacovigilance review required; no validated E2B/R3 export is produced.",
    ]
    VALIDATION_OUT.write_text("\n".join(validation) + "\n", encoding="utf-8")
    print("\n".join(validation))
    print(f"Created: {JSON_OUT.name}, {NARRATIVE_OUT.name}, {VALIDATION_OUT.name}")

if __name__ == "__main__":
    main()
