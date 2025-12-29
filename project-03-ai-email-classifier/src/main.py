import argparse
import sys

from preprocess import preprocess_email
from classify import call_llm, parse_or_repair
from postprocess import validate_result, save_outputs


def read_text_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def main():
    parser = argparse.ArgumentParser(description="AI Email Classifier (raw email text -> JSON)")
    parser.add_argument("--input", required=True, help="Path to raw email text file")
    parser.add_argument("--out", default="outputs", help="Output directory (default: outputs)")
    parser.add_argument("--no-redact", action="store_true", help="Disable basic PII redaction")
    args = parser.parse_args()

    raw = read_text_file(args.input)

    pre = preprocess_email(raw, do_redact=(not args.no_redact))
    clean_text = pre["clean_text"]
    notes = pre["notes"]

    # Call OpenAI
    output_text = call_llm(clean_text)

    # Parse JSON, repair if needed
    result, repaired = parse_or_repair(output_text)

    # Validate and enforce minimal correctness
    errors = validate_result(result)
    if errors:
        # Fail safe: mark for human review if output is shaky
        result["needs_human_review"] = True
        result["tags"] = list(set(result.get("tags", []) + ["validation_warning"]))
        result["summary"] = (result.get("summary") or "").strip()[:500]
        # Provide a short note in intent if missing
        if not result.get("intent"):
            result["intent"] = "Unclear; requires manual review."

    paths = save_outputs(args.out, clean_text, notes, result, repaired)

    print("Classification complete.")
    print(f"Saved JSON:  {paths['json']}")
    print(f"Audit JSONL: {paths['jsonl']}")
    print("\nResult preview:")
    print(f"- category: {result.get('category')}")
    print(f"- priority: {result.get('priority')}")
    print(f"- needs_human_review: {result.get('needs_human_review')}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nCancelled.")
        sys.exit(1)
