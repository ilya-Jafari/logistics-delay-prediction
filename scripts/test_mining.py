import requests
from bs4 import BeautifulSoup

def test_fetch_rss():
    print("🌐 Connecting to gCaptain Logistics RSS Feed...")
    url = "https://gcaptain.com/feed/" 
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.content, 'xml')
        
        headlines = [item.text.strip() for item in soup.find_all('title')]
        
        actual_news = headlines[1:6] 
        
        if not actual_news:
            print("❌ Still blocked or empty. Let's use Simulated Data for now.")
            return None
        else:
            print(f"✅ Success! Mined {len(actual_news)} live headlines:")
            for i, h in enumerate(actual_news, 1):
                print(f"{i}. {h}")
            return actual_news
                
    except Exception as e:
        print(f"⚠️ Error: {e}")
        return None

if __name__ == "__main__":
    test_fetch_rss()