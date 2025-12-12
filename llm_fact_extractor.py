from openai import OpenAI

client = OpenAI()  # uses OPENAI_API_KEY from environment

def extract_facts_from_text(text, topic="General"):
    """
    Send PYQ text to GPT-5-mini to extract short factual statements.
    Returns a list of facts.
    """
    prompt = f"""
You are an UPSC exam expert.
Extract pure factual statements (1-2 lines each) from the following text.
Only facts, no explanations.
Topic: {topic}

Text:
{text}
"""
    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    fact_text = response.output_text.strip()
    facts = [f.strip() for f in fact_text.split("\n") if f.strip()]
    return facts
