# Project 01 – AI Lead Classifier (OpenAI)

This project is a production-style AI automation that classifies business leads using the OpenAI API.

## What it does
- Takes a CSV file of leads as input
- Uses an LLM to classify lead value
- Outputs both JSON and CSV files
- Demonstrates secure API usage and modular design

## Tech Stack
- Python
- OpenAI API
- dotenv
- CSV / JSON

## How to run
1. Install dependencies  
   `pip install -r requirements.txt`

2. Create `.env` file  
   Add your OpenAI API key

3. Run  
   `python3 src/main.py`

## Output
- `classified_leads.json`
- `classified_leads.csv`
