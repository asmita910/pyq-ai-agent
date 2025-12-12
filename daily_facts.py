import random
from progress_tracker import load_progress, add_fact_learned, add_fact_forgotten

DAILY_FACT_COUNT = 5

def generate_daily_facts():
    data = load_progress()
    all_facts = data.get("facts_learned", [])
    forgotten_facts = data.get("facts_forgotten", [])

    # Remove already forgotten facts from daily selection
    available_facts = [f for f in all_facts if f not in forgotten_facts]

    if not available_facts:
        print("No facts available. Process PDFs first!")
        return []

    # Pick 5 random facts
    daily_facts = random.sample(available_facts, min(DAILY_FACT_COUNT, len(available_facts)))
    return daily_facts

if __name__ == "__main__":
    facts = generate_daily_facts()
    print("📌 Daily 5 Facts:")
    for i, fact in enumerate(facts, 1):
        print(f"{i}. {fact}")
