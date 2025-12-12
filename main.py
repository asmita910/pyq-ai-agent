from utils.pdf_extractor import extract_text_from_pdf
from utils.fact_extractor import extract_facts_from_text

pdf_path = "data/pyq_pdfs/2024.pdf"

text = extract_text_from_pdf(pdf_path)
facts = extract_facts_from_text(text)

for f in facts[:20]:
    print(f)
