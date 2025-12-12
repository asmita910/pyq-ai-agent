from utils.pdf_extractor import extract_text_from_pdf
from utils.fact_extractor import extract_facts_from_text
from progress_tracker import mark_pdf_processed, add_fact_learned

pdf_path = "data/pyq_pdfs/2024.pdf"

text = extract_text_from_pdf(pdf_path)
#facts = extract_facts_from_text(text)
facts = extract_facts_from_text(text, topic="Polity")
for i, f in enumerate(facts[:10], 1):
    print(f"{i}. {f}")
# Mark PDF processed
mark_pdf_processed(pdf_path)

# Show first 10 facts
for f in facts[:10]:
    print(f)
    add_fact_learned(f)  # store in progress file

