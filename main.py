from agents.alert_agent import alert_agent
from agents.analysis_agent import analysis_agent
from agents.decision_agent import decision_agent
from agents.response_agent import response_agent
from agents.memory_agent import memory_agent

import os

LOG_FILE = "logs/incidents.txt"


def is_valid_alert(line):
    """
    Filter only meaningful alerts
    """
    keywords = ["cpu", "memory", "error", "fail", "unauthorized", "timeout", "disk", "network"]
    return any(k in line.lower() for k in keywords)


def run_system(user_input):
    print("\n🚀 AI Incident Commander Started\n")

    data = alert_agent(user_input)
    analysis = analysis_agent(data)
    repeated = memory_agent(analysis)
    decision = decision_agent(analysis)

    # boost priority if repeated issue
    if repeated:
        decision["priority"] = "CRITICAL"
        decision["recommended_action"] += " | Immediate escalation required"

    response_agent(analysis, decision)


# 🔥 Run ONCE mode (optimized)
if __name__ == "__main__":
    print("📡 Processing ONE incident only...\n")

    if not os.path.exists(LOG_FILE):
        print("❌ Log file not found:", LOG_FILE)
        exit(1)

    with open(LOG_FILE, "r") as f:
        lines = f.readlines()

    processed = False

    for line in lines:
        line = line.strip()

        # skip junk
        if not line or line.startswith("="):
            continue

        # only process meaningful alerts
        if is_valid_alert(line):
            print(f"\n⚠️ Processing Alert: {line}")
            run_system(line)
            processed = True
            break  # 🔥 VERY IMPORTANT → only ONE alert

    if not processed:
        print("✅ No valid alerts found.")

    print("\n✅ Done. Exiting.")
