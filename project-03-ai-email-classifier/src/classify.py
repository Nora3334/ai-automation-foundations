import json
import os
from typing import Any, Dict, Tuple

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


SYSTEM_INSTRUCTION = """You are an AI assistant for a small business inbox.
Your job: classify incoming emails for routing and response drafting.

You MUST return ONLY valid JSON matching the schema exactly.
No markdown. No extra commentary.
"""

SCHEMA_DESCRIPTION = """Return JSON with these keys:
- category: one of ["Sales","Support","Billing","Partnership","Spam","Other"]
- priority: one of ["High","Medium","Low"]
- intent: string (one sentence)
- summary: string (1-2 sentences)
- suggested_response: string (professional reply draft)
- confidence: number between 0 and 1
- needs_human_review: boolean
- tags: array of short strings

Rules:
- If the email mentions payment/refund/invoice -> category="Billing"
- If it requests pricing/quote/demo -> category="Sales"
- If it reports a problem/outage/how-to -> category="Support"
- If it proposes collaboration/partnership -> category="Partnership"
- If it is clearly junk/irrelevant -> category="Spam"
- Otherwise -> category="Other"

Set needs_human_review=true when:
- confidence < 0.65, OR
- category is Billing and it mentions charge disputes/refunds, OR
- the message is ambiguous or asks for legal/contract commitments.
"""


def call_llm(email_text: str) -> str:
    prompt = f"""{SCHEMA_DESCRIPTION}

EMAIL:
{email_text}
"""

    resp = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_INSTRUCTION},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=500,
    )
    return resp.choices[0].message.content


def repair_to_json(bad_output: str) -> str:
    """
    If model returns non-JSON, ask it to output valid JSON only.
    """
    repair_prompt = f"""Fix the following so it becomes valid JSON ONLY.
No markdown, no backticks, no explanations.

CONTENT:
{bad_output}
"""
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a JSON formatter. Output ONLY valid JSON."},
            {"role": "user", "content": repair_prompt}
        ],
        temperature=0.0,
        max_tokens=500,
    )
    return resp.choices[0].message.content


def parse_or_repair(output_text: str) -> Tuple[Dict[str, Any], bool]:
    """
    Returns (parsed_json, repaired_flag)
    """
    try:
        return json.loads(output_text), False
    except json.JSONDecodeError:
        repaired = repair_to_json(output_text)
        return json.loads(repaired), True
