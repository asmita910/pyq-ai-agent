import json
import os

PROGRESS_FILE = "data/progress.json"

def load_progress():
    if not os.path.exists(PROGRESS_FILE):
        return {"facts_learned": [], "facts_forgotten": [], "pdfs_processed": []}
    with open(PROGRESS_FILE, "r") as f:
        return json.load(f)

def save_progress(data):
    with open(PROGRESS_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_fact_learned(fact):
    data = load_progress()
    if fact not in data["facts_learned"]:
        data["facts_learned"].append(fact)
    save_progress(data)

def add_fact_forgotten(fact):
    data = load_progress()
    if fact not in data["facts_forgotten"]:
        data["facts_forgotten"].append(fact)
    save_progress(data)

def mark_pdf_processed(pdf_name):
    data = load_progress()
    if pdf_name not in data["pdfs_processed"]:
        data["pdfs_processed"].append(pdf_name)
    save_progress(data)
