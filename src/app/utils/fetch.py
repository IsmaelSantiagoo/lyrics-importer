import requests
from bs4 import BeautifulSoup

def fetch_lyrics(url: str) -> str:
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")

    letra = soup.select_one(".lyric-original")
    if not letra:
        raise Exception("Letra não encontrada na página")

    return letra.get_text("\n", strip=True)
