import json
import os
import time
import hashlib
from typing import Any, Dict, List


ALLOWED_CATEGORIES = {"Sales", "Support", "Billing", "Partnership", "Spam", "Other"}
ALLOWED_PRIORITY = {"High", "Medium", "Low"}


def validate_result(obj: Dict[str, Any]) -> List[str]:
    errors = []

    if obj.get("category") not in ALLOWED_CATEGORIES:
        errors.append("Invalid category")
    if obj.get("priority") not in ALLOWED_PRIORITY:
        errors.append("Invalid priority")

    for k in ["intent", "summary", "suggested_response"]:
        if not isinstance(obj.get(k), str) or not obj.get(k).strip():
            errors.append(f"Missing/invalid {k}")

    conf = obj.get("confidence")
    if not isinstance(conf, (int, float)) or not (0 <= float(conf) <= 1):
        errors.append("Invalid confidence")

    if not isinstance(obj.get("needs_human_review"), bool):
        errors.append("needs_human_review must be boolean")

    tags = obj.get("tags")
    if not isinstance(tags, list):
        errors.append("tags must be array")
    else:
        # Keep tags short
        obj["tags"] = [str(t)[:30] for t in tags][:10]

    return errors


def stable_email_id(email_text: str) -> str:
    h = hashlib.sha256(email_text.encode("utf-8")).hexdigest()[:10]
    return h


def save_outputs(
    output_dir: str,
    email_text: str,
    preproc_notes: str,
    result: Dict[str, Any],
    repaired: bool
) -> Dict[str, str]:
    os.makedirs(output_dir, exist_ok=True)
    ts = time.strftime("%Y%m%d_%H%M%S")
    eid = stable_email_id(email_text)

    record = {
        "email_id": eid,
        "timestamp": ts,
        "preprocess_notes": preproc_notes,
        "repaired_json": repaired,
        "result": result,
    }

    json_path = os.path.join(output_dir, f"{ts}_{eid}.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(record, f, indent=2)

    jsonl_path = os.path.join(output_dir, "run_log.jsonl")
    with open(jsonl_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")

    return {"json": json_path, "jsonl": jsonl_path}
