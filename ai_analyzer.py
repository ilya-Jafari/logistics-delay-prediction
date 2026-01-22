import ollama

# Simple function to ask Llama 3 for a logistics insight
def analyze_logistics_risk(delay_prob, region, product):
    prompt = f"""
    As a professional logistics consultant, analyze this scenario:
    - A shipment of {product} is going to {region}.
    - Our AI model predicts a {delay_prob:.2%} probability of delay.
    
    Provide a brief, 2-line strategic advice for the manager to mitigate this risk.
    """
    
    response = ollama.chat(model='llama3', messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])
    
    return response['message']['content']

# Example usage
risk_score = 0.78  # 78% risk from our previous model
target_region = "Southeast Asia"
item = "Smartphones"

print("--- AI Logistics Consultant ---")
insight = analyze_logistics_risk(risk_score, target_region, item)
print(insight)