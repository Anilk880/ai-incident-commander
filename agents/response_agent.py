import os
from datetime import datetime

LOG_FILE = "logs/incidents.txt"


def save_log(analysis, decision):
    os.makedirs("logs", exist_ok=True)

    with open(LOG_FILE, "a") as f:
        f.write("\n============================\n")
        f.write(f"Time: {datetime.now()}\n")
        f.write(f"Severity: {analysis['severity']}\n")
        f.write(f"Root Cause: {analysis['root_cause']}\n")
        f.write(f"Explanation: {analysis['explanation']}\n")
        f.write(f"Action Required: {decision['action_required']}\n")
        f.write(f"Recommendation: {decision['recommended_action']}\n")
        f.write(f"Priority: {decision['priority']}\n")
        f.write(f"Command: {decision.get('command', 'N/A')}\n")
        f.write("============================\n")


def response_agent(analysis, decision):
    print("\n[Response Agent] Taking action...")

    print("\n===== 🚀 AI INCIDENT COMMANDER REPORT =====\n")

    print(f"🔥 Severity       : {analysis['severity']}")
    print(f"🧠 Root Cause    : {analysis['root_cause']}")
    print(f"📖 Explanation   : {analysis['explanation']}\n")

    print(f"⚡ Action Needed : {decision['action_required']}")
    print(f"🛠️ Recommendation: {decision['recommended_action']}")
    print(f"🚨 Priority      : {decision['priority']}\n")

    if decision.get("command"):
        print(f"💻 Suggested Command:\n{decision['command']}")

    # Save log
    save_log(analysis, decision)

    print("\n📝 Log saved to logs/incidents.txt")
