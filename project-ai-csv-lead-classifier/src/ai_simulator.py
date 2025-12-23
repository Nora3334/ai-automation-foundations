def simulate_ai_classification(leads):
    results = []

    for lead in leads:
        score = lead["engagement_score"]

        if score >= 80:
            category = "hot"
            priority = "high"
        elif score >= 60:
            category = "warm"
            priority = "medium"
        else:
            category = "cold"
            priority = "low"

        results.append({
            "name": lead["name"],
            "email": lead["email"],
            "lead_category": category,
            "priority": priority,
            "reasoning": f"Engagement score of {score} determines classification."
        })

    return results

