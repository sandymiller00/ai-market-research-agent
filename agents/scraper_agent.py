import requests
from bs4 import BeautifulSoup


class ScraperAgent:
    """Scrapes readable text from a webpage."""

    def __init__(self):
        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/137.0.0.0 Safari/537.36"
            )
        }

    def scrape(self, url: str) -> str:
        """Scrape and return clean text from a webpage."""

        try:
            response = requests.get(
                url,
                headers=self.headers,
                timeout=10,
            )

            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            # Remove unwanted HTML tags
            for tag in soup(["script", "style", "noscript"]):
                tag.decompose()

            text = soup.get_text(separator=" ", strip=True)

            return text

        except Exception as error:
            print(f"Scraping Error: {error}")
            return ""
