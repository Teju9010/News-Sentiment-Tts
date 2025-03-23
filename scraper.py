
import requests
from bs4 import BeautifulSoup

def fetch_news(company):
    search_url = f"https://news.google.com/rss/search?q={company}&hl=en-IN&gl=IN&ceid=IN:en"

    try:
        response = requests.get(search_url)
        response.raise_for_status()  # Raise an error for bad responses (e.g., 404)

        soup = BeautifulSoup(response.content, "xml") 
        articles = []

        for item in soup.find_all("item")[:10]:  
            title = item.title.text
            link = item.link.text
            summary = item.description.text if item.description else "No summary available"
            
            articles.append({"title": title, "link": link, "summary": summary})

        return articles

    except requests.exceptions.RequestException as e:
        print(f"Error fetching news articles: {e}")
        return []




