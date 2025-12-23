# AI Lead Classification Automation (CSV → AI → JSON)

## Overview
This project demonstrates an end-to-end AI automation pipeline that classifies business leads using structured input data and an AI-style decision layer.

## Business Problem
Small businesses receive lead data in CSV format from forms, CRMs, or marketing tools. Manually prioritizing leads is slow and inconsistent.

## Solution Architecture
1. CSV ingestion and validation
2. Data preprocessing
3. AI decision simulation (LLM-ready)
4. Structured JSON output for downstream automation

## AI Design
Instead of calling a live LLM, this project simulates AI behavior using:
- A production-style prompt
- Deterministic classification logic

This design allows easy migration to real LLM APIs.

## Input
- CSV file containing lead details and engagement scores

## Output
- JSON file with lead category, priority, and reasoning

## Tech Stack
- Python
- CSV / JSON
- Modular automation architecture

## Future Enhancements
- Replace simulator with OpenAI / Azure OpenAI API
- Add webhook or CRM integration
- Confidence scoring using LLM reasoning

## Outcome
A production-style AI automation system suitable for SMBs, consultants, and internal automation teams.

