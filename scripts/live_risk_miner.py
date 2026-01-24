import requests
from bs4 import BeautifulSoup
import ollama

# 1. Scraping: Mining the latest logistics headlines
def fetch_logistics_news():
    url = "https://www.supplychainbrain.com/articles" # Example 2026 news source
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extracting headlines (structure based on common 2026 web standards)
    headlines = [h.text.strip() for h in soup.find_all('h2')[:5]] 
    return headlines

# 2. AI Analysis: Feeding live news to Llama 3
def analyze_current_risks(news_list):
    news_context = "\n- ".join(news_list)
    prompt = f"""
    Current Logistics Headlines:
    - {news_context}
    
    Based on these headlines from 2026, identify the TOP 2 GLOBAL RISKS 
    that could delay shipments this week. Be concise.
    """
    
    response = ollama.chat(model='llama3', messages=[
        {'role': 'user', 'content': prompt}
    ])
    return response['message']['content']

# Execution
print("🔍 Mining live logistics data...")
latest_news = fetch_logistics_news()
if latest_news:
    print(f"✅ Found {len(latest_news)} recent updates.")
    print("\n🤖 Llama 3 Analysis of Current Global Situation:")
    analysis = analyze_current_risks(latest_news)
    print(analysis)