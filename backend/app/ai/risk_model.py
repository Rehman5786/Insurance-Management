import random

def calculate_risk(city: str):
    # Mock logic (later replace with XGBoost)
    
    high_risk_cities = ["Chennai", "Mumbai", "Kolkata"]
    
    if city in high_risk_cities:
        risk_score = round(random.uniform(0.5, 0.9), 2)
    else:
        risk_score = round(random.uniform(0.1, 0.5), 2)

    expected_loss = round(risk_score * 100, 2)

    return risk_score, expected_loss