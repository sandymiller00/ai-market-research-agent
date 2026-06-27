from agents.scraper_agent import ScraperAgent

scraper = ScraperAgent()

url = "https://www.tesla.com"

text = scraper.scrape(url)

print(text[:1000])
