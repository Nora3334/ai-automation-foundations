import json
from pre_processing import load_leads
from ai_classifier import classify_lead
from post_processing import save_json, save_csv

INPUT_CSV = "data/input_leads.csv"
OUTPUT_JSON = "data/classified_leads.json"
OUTPUT_CSV = "data/classified_leads.csv"

def main():
    leads = load_leads(INPUT_CSV)
    results = []

    for lead in leads:
        classification = classify_lead(lead)
        classification_data = json.loads(classification)

        results.append({
            "lead": lead,
            "classification": classification_data
        })

    save_json(results, OUTPUT_JSON)
    save_csv(results, OUTPUT_CSV)

    print("Lead classification completed successfully.")

if __name__ == "__main__":
    main()
