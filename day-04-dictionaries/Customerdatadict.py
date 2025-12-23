# Day 4: Customer data stored in dictionaries

customers = [
    {
        "name": "Alice",
        "email": "alice@gmail.com",
        "industry": "Real Estate",
        "leads": 5,
        "is_active": True
    },
    {
        "name": "Bob",
        "email": "bob@yahoo.com",
        "industry": "E-commerce",
        "leads": 12,
        "is_active": False
    },
    {
        "name": "Charlie",
        "email": "charlie@company.com",
        "industry": "Real Estate",
        "leads": 8,
        "is_active": True
    }
]

# Summaries
total_customers = len(customers)
total_leads = 0
active_customers = 0
industry_summary = {}

for customer in customers:
    total_leads += customer["leads"]

    if customer["is_active"]:
        active_customers += 1

    industry = customer["industry"]
    if industry not in industry_summary:
        industry_summary[industry] = 1
    else:
        industry_summary[industry] += 1

print("---- Customer Summary ----")
print(f"Total customers: {total_customers}")
print(f"Total leads: {total_leads}")
print(f"Active customers: {active_customers}")

print("\nCustomers by industry:")
for industry, count in industry_summary.items():
    print(f"- {industry}: {count}")
