import json
from utils.config import client, MODEL
from agents.analysis_agent import extract_json

def decision_agent(analysis):
    print("\n[Decision Agent] Deciding action...")

    prompt = f"""
    You are an incident response system.

    Based on:
    {analysis}

    Return ONLY JSON:
    {{
      "action_required": "YES/NO",
      "recommended_action": "...",
      "priority": "LOW/MEDIUM/HIGH",
      "command": "bash/kubectl command if possible"
    }}
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    raw = response.choices[0].message.content
    parsed = extract_json(raw)

    print("[Decision Parsed]", parsed)

    return parsed
