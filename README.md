# AI Market Research Agent

A Python tool that automates market research using AI. You give it a topic, it searches the web, reads the content, analyzes it using GPT, and gives you a clean PDF report.

---

## What it does

Manual market research takes a lot of time — searching sites, reading articles, comparing sources, then writing a report. This tool does all of that automatically.

You type a topic like **"Electric Vehicle Market in India"** and it:

1. Searches the web for relevant sources
2. Scrapes and extracts content from those pages
3. Sends everything to GPT for analysis
4. Generates a PDF report with sections like trends, competitors, risks, and recommendations

---

## How it works

The project has 4 agents, each with one job:

- **Search Agent** — uses Tavily API to find relevant URLs
- **Scraper Agent** — visits each URL and extracts the text using BeautifulSoup
- **Analysis Agent** — sends the text to OpenAI GPT and gets a structured analysis
- **Report Agent** — converts the analysis into a PDF using ReportLab

---

## Tech stack

- Python
- OpenAI GPT (for analysis)
- Tavily API (for web search)
- BeautifulSoup + Requests (for scraping)
- ReportLab (for PDF generation)
- python-dotenv (for API key management)

---

## Getting started

```bash
git clone https://github.com/your-username/ai-market-research-agent.git
cd ai-market-research-agent
```

Create a `.env` file with your API keys:

```
OPENAI_API_KEY=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
TAVILY_API_KEY=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

```

Install dependencies and run:

```bash
pip install -r requirements.txt
python main.py
```

---

## Output

The generated PDF report is saved in the `reports/` folder. It includes:

- Executive Summary
- Market Overview
- Industry Trends
- Competitor Analysis
- Opportunities & Risks
- Recommendations
- Conclusion

---

## Limitations

- Needs an internet connection
- Depends on OpenAI and Tavily APIs (paid)
- AI-generated content — always review before using for important decisions

---

## Planned improvements

- FastAPI backend
- React frontend
- LangGraph multi-agent orchestration
- Database for report history
- Cloud deployment

---

## Who can use this

Business analysts, startup founders, students, consultants, or anyone who needs a quick market overview without spending hours researching manually.

---
