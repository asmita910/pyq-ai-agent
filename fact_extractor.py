def extract_facts_from_text(text):
    """Turns PYQ question text into short, to-the-point facts."""
    # Placeholder — we will implement this gradually
    lines = text.split("\n")
    facts = []

    for line in lines:
        line = line.strip()
        if len(line.split()) > 6:   # ignore too-short lines
            facts.append(line)

    return facts
