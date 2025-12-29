# Project 03 – AI Email Classifier (Raw Email → AI → JSON)

## Overview
A production-style AI automation that classifies inbound email text for a generic small business inbox and produces structured JSON outputs suitable for routing, automation, and response drafting.

## Input
- Raw email text file (e.g., `samples/email_01_sales.txt`)

## Output
- Per-email JSON file in `outputs/` (timestamp + stable hash)
- Append-only audit log `outputs/run_log.jsonl`

## What the AI Produces
- category: Sales / Support / Billing / Partnership / Spam / Other
- priority: High / Medium / Low
- intent, summary
- suggested_response
- confidence (0–1)
- needs_human_review (safety flag)
- tags

## Reliability Features
- Preprocessing: trims long threads + optional basic PII redaction
- JSON-only contract + automatic repair pass if parsing fails
- Validation: forces `needs_human_review=true` if output is inconsistent

## Setup
1) Install dependencies
```bash
pip3 install -r requirements.txt
