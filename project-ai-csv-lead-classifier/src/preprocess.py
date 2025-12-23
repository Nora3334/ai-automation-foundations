import csv

def load_leads(file_path):
    leads = []
    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row["engagement_score"] = int(row["engagement_score"])
            leads.append(row)
    return leads

