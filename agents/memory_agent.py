memory_store = []

def normalize(text):
    return text.lower().strip()


def is_similar(a, b):
    a = normalize(a)
    b = normalize(b)

    keywords = ["cpu", "database", "timeout"]

    match_count = sum(1 for k in keywords if k in a and k in b)

    return match_count >= 2  # threshold


def memory_agent(analysis):
    print("\n[Memory Agent] Checking history...")

    repeated = False

    for past in memory_store:
        if is_similar(past["root_cause"], analysis["root_cause"]):
            repeated = True
            break

    memory_store.append(analysis)

    if repeated:
        print("⚠️ Repeated Incident Detected!")
        return True

    return False
