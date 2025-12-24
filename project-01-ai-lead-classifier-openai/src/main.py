import os
from preprocess import load_leads
from ai_simulator import simulate_ai_classification
from postprocess import save_json, save_csv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_CSV = os.path.join(BASE_DIR, "../data/leads.csv")
OUTPUT_JSON = os.path.join(BASE_DIR, "../data/classified_leads.json")
OUTPUT_CSV = os.path.join(BASE_DIR, "../data/classified_leads.csv")

def main():
    leads = load_leads(INPUT_CSV)
    ai_results = simulate_ai_classification(leads)

    save_json(ai_results, OUTPUT_JSON)
    save_csv(ai_results, OUTPUT_CSV)

    print("Lead classification completed successfully.")
    print("Outputs generated:")
    print("- JSON:", OUTPUT_JSON)
    print("- CSV:", OUTPUT_CSV)

if __name__ == "__main__":
    main()
