import os
from dotenv import load_dotenv
from tavily import TavilyClient

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("TAVILY_API_KEY")

print("API Key:", api_key)

# Create client
client = TavilyClient(api_key=api_key)

# Search
response = client.search(query="Tesla company overview", max_results=3)

print("\nResponse:")
print(response)
