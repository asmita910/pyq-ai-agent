import streamlit as st
from daily_facts import generate_daily_facts
from progress_tracker import add_fact_forgotten

st.set_page_config(page_title="PYQ AI Agent", layout="centered")

st.title("📘 PYQ AI Revision Agent")

st.write("Daily facts generated purely from PYQs you studied.")

# Generate Daily Facts
if st.button("Generate Daily 5 Facts"):
    facts = generate_daily_facts()

    if not facts:
        st.warning("No facts available. Please process PDFs first.")
    else:
        for i, fact in enumerate(facts, 1):
            col1, col2 = st.columns([8, 2])
            col1.write(f"**{i}.** {fact}")
            if col2.button("Forgot", key=fact):
                add_fact_forgotten(fact)
                st.success("Marked as forgotten")

st.divider()

st.caption("Built for serious exam aspirants using PYQs only.")
