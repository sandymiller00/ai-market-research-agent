from tavily import TavilyClient
from config import TAVILY_API_KEY


class SearchAgent:

    def __init__(self):
        self.client = TavilyClient(api_key=TAVILY_API_KEY)

    def search_company(self, company_name):
        return self.client.search(
            query=f"{company_name} company overview",
            max_results=5,
        )
