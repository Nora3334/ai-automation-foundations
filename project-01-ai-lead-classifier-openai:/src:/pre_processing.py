import csv

def load_leads(csv_path):
    leads = []

    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            leads.append(row)

    return leads
