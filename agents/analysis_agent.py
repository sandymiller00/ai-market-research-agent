from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def analyze(topic, research):
    prompt = f"""
You are a senior market research analyst.

Research Topic:
{topic}

Research Data:
{research}

Generate:

1. Executive Summary

2. Market Overview

3. Trends

4. Opportunities

5. Competitors

6. Risks

7. Recommendations

8. Conclusion
"""

    response = client.chat.completions.create(
        model="gpt-4.1", messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
