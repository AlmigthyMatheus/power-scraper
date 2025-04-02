import requests

RAPIDAPI_KEY = "f711eaf34fmsh4cb61e9933ce8d5p1075c6jsnf9393e6ac767"
SCRAPER_URL = "https://ai-web-scraper1.p.rapidapi.com/"

headers = {
    "x-rapidapi-key": RAPIDAPI_KEY,
    "x-rapidapi-host": "ai-web-scraper1.p.rapidapi.com",
    "Content-Type": "application/json"
}

def raspar_url(url):
    payload = {
        "url": url,
        "summary": True
    }
    resposta = requests.post(SCRAPER_URL, json=payload, headers=headers)
    return resposta.json()
