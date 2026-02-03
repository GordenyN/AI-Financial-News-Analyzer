from fastapi import FastAPI
import requests
from datetime import datetime
import trafilatura

app = FastAPI()

NEWS_API_KEY = ".env"

ALLOWED_SITES = [
    "yahoo.com",
    "reuters.com",
    "cnbc.com",
    "marketwatch.com",
    "finance.yahoo.com"
]

def is_allowed(url: str) -> bool:
    return any(site in url for site in ALLOWED_SITES)

def extract_clean_text(url: str) -> str:
    downloaded = trafilatura.fetch_url(url)
    if not downloaded:
        return ""
    text = trafilatura.extract(downloaded, include_comments=False, include_images=False)
    return text or ""

@app.get("/summarize")
def summarize(topic: str = "finance"):
    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={topic}&sortBy=publishedAt&language=en&apiKey={NEWS_API_KEY}"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Не удалось получить новости", "status_code": response.status_code}

    news = response.json().get("articles", [])

    filtered = [article for article in news if is_allowed(article["url"])]

    result = []
    for article in filtered[:10]:   
        clean_text = extract_clean_text(article["url"])
        result.append({
            "title": article["title"],
            "url": article["url"],
            "text": clean_text
        })

    return {
        "date": str(datetime.now()),
        "topic": topic,
        "total_articles": len(result),
        "articles": result
    }
