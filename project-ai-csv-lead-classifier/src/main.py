from preprocess import load_leads
from ai_simulator import simulate_ai_classification
from postprocess import save_results

INPUT_CSV = "../data/leads.csv"
OUTPUT_JSON = "../data/classified_leads.json"

def main():
    leads = load_leads(INPUT_CSV)
    ai_results = simulate_ai_classification(leads)
    save_results(ai_results, OUTPUT_JSON)
    print("Lead classification completed successfully.")

if __name__ == "__main__":
    main()

