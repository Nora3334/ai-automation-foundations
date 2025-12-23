import json

try:
    # Intentionally wrong filename to test error handling
    with open("missing_file.json", "r") as file:
        customers = json.load(file)

except FileNotFoundError:
    print("ERROR: File not found. Please check the file name.")
    customers = []

except json.JSONDecodeError:
    print("ERROR: File is not valid JSON.")
    customers = []

# Continue safely even after failure
for customer in customers:
    try:
        name = customer["name"]
        score = customer["score"]
        print(f"{name} has a score of {score}")
    except KeyError as e:
        print(f"WARNING: Missing key {e} in customer record:", customer)

print("Script finished safely.")
