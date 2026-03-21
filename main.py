from agents.alert_agent import alert_agent
from agents.analysis_agent import analysis_agent
from agents.decision_agent import decision_agent
from agents.response_agent import response_agent
from agents.memory_agent import memory_agent


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


# 🔥 Continuous Mode
if __name__ == "__main__":
    while True:
        user_input = input("\nEnter alert (or type 'exit'): ")

        if user_input.lower() == "exit":
            break

        run_system(user_input)
