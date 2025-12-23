import json

def save_results(results, output_path):
    with open(output_path, "w") as file:
        json.dump(results, file, indent=4)

