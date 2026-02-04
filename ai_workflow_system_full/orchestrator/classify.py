
def classify_prompt(query):
    return {
        "domains": [{"domain": "engineering", "weight": 0.8}],
        "intent": "learn",
        "needs_retrieval": True
    }
