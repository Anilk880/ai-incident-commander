import json
from utils.config import client, MODEL

def extract_json(text):
    text = text.strip()

    if "```json" in text:
        text = text.split("```json")[1].split("```")[0]

    return json.loads(text)


def analysis_agent(data):
    print("\n[Analysis Agent] Finding root cause...")

    prompt = f"""
    You are a senior SRE engineer.

    Analyze this alert:
    {data['alert']}

    Return ONLY JSON:
    {{
      "root_cause": "...",
      "severity": "LOW/MEDIUM/HIGH",
      "explanation": "..."
    }}
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    raw = response.choices[0].message.content
    parsed = extract_json(raw)

    print("[Analysis Parsed]", parsed)

    return parsed
