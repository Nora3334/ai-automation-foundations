import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def classify_lead(lead):
    prompt = f"""
You are an AI assistant that classifies business leads.

Lead details:
Name: {lead['name']}
Company: {lead['company']}
Source: {lead['source']}

Classify this lead as one of:
- High Value
- Medium Value
- Low Value

Return ONLY valid JSON like:
{{"lead_score": "High Value", "reason": "short explanation"}}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content
