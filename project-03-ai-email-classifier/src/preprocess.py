import re
from typing import Dict


def redact_pii(text: str) -> str:
    """
    Very lightweight PII redaction (not perfect).
    Redacts:
      - emails
      - phone-like patterns
    """
    text = re.sub(r"[\w\.-]+@[\w\.-]+\.\w+", "[REDACTED_EMAIL]", text)
    text = re.sub(r"\b(\+?\d[\d\-\s\(\)]{7,}\d)\b", "[REDACTED_PHONE]", text)
    return text


def trim_email_thread(text: str, max_chars: int = 6000) -> str:
    """
    Keep the newest part of the email and reduce long quoted threads.
    Heuristic: cut off after common reply separators if present.
    """
    separators = [
        "\nOn ",          # common reply format: On Mon, ...
        "\nFrom:",        # Outlook-like
        "\n-----Original Message-----",
        "\n________________________________",
    ]

    cut_index = None
    for sep in separators:
        idx = text.find(sep)
        if idx != -1:
            cut_index = idx
            break

    if cut_index is not None:
        text = text[:cut_index]

    text = text.strip()

    if len(text) > max_chars:
        text = text[:max_chars].rstrip() + "\n\n[TRIMMED]"
    return text


def preprocess_email(raw_text: str, do_redact: bool = True) -> Dict[str, str]:
    """
    Returns a dict with cleaned text and a note of what was done.
    """
    original_len = len(raw_text)
    cleaned = trim_email_thread(raw_text)

    redaction_applied = False
    if do_redact:
        redacted = redact_pii(cleaned)
        redaction_applied = (redacted != cleaned)
        cleaned = redacted

    return {
        "clean_text": cleaned,
        "notes": f"original_len={original_len}, cleaned_len={len(cleaned)}, redaction={redaction_applied}"
    }
