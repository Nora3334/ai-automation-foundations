import json
import csv

def save_json(results, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

def save_csv(results, output_path):
    with open(output_path, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["name", "email", "company", "source", "lead_score", "reason"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for item in results:
            row = item["lead"]
            row.update(item["classification"])
            writer.writerow(row)
