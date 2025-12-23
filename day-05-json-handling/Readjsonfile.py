import json

# Read JSON file
with open("customers.json", "r") as file:
    customers = json.load(file)

# Modify data
for customer in customers:
    if customer["score"] >= 80:
        customer["status"] = "hot"
    elif customer["score"] >= 60:
        customer["status"] = "warm"
    else:
        customer["status"] = "cold"

# Add a new field
for customer in customers:
    customer["contacted"] = False

# Write updated JSON back to file
with open("customers_updated.json", "w") as file:
    json.dump(customers, file, indent=4)

print("Customer data updated and saved to customers_updated.json")


# ---- AI SIMULATION (Mock LLM Integration) ----

print("\n--- Simulated AI Lead Classification ---")

with open("mock_ai_response.json", "r") as file:
    ai_results = json.load(file)

for result in ai_results:
    print(
        f"Customer: {result['name']} | "
        f"AI Category: {result['lead_category']} | "
        f"Reason: {result['reasoning']}"
    )
