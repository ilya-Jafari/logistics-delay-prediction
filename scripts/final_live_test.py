import ollama

live_headlines = [
    "FMC Commissioners Confirm Trump Administration Is Closing Longstanding Harbor Maintenance Tax Loophole",
    "New Trade Map Takes Shape in Davos as World Adjusts to Trump Tariffs",
    "U.S. Coast Guard Seizes $7M in Cocaine from Drug-Smuggling Boat North of Puerto Rico",
    "NOAA Launches Deep-Sea Mapping Project Off American Samoa as Critical Minerals Race Accelerates"
]

def final_risk_report(news):
    print("🧠 Llama 3 is processing live 2026 trade data...")
    
    prompt = f"""
    You are a Senior Supply Chain Risk Analyst. 
    Analyze these 2026 headlines:
    {news}
    
    Questions to answer:
    1. Which headline causes the most 'Financial Risk' for importers?
    2. Which one indicates a 'Geopolitical Shift' in trade routes?
    
    Provide a professional 3-sentence summary.
    """
    
    response = ollama.chat(model='llama3', messages=[
        {'role': 'user', 'content': prompt}
    ])
    
    print("\n" + "="*40)
    print("🚀 LIVE LOGISTICS INTELLIGENCE REPORT")
    print("="*40)
    print(response['message']['content'])

if __name__ == "__main__":
    final_risk_report(live_headlines)