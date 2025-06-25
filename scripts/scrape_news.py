# scripts/scrape_news.py

import requests
from bs4 import BeautifulSoup

def get_headlines():
    url = "https://elpais.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = []
    for tag in soup.find_all("h2"):
        text = tag.get_text(strip=True)
        if text:
            headlines.append(text)

    return headlines[:10]  # Solo los 10 primeros

if __name__ == "__main__":
    for i, headline in enumerate(get_headlines(), 1):
        print(f"{i}. {headline}")
