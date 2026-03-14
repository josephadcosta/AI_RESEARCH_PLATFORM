# app/streamlit_app.py
import sys
import os
import streamlit as st
import pandas as pd
import PyPDF2

# Ensure parent directory is visible to import scripts
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from my_scripts.summarizer import summarize

st.set_page_config(page_title="AI Research Insight Generator", layout="wide")
st.title("AI Research Insight Generator")

# --- PDF Upload ---
uploaded = st.file_uploader("Upload research paper (PDF)", type=["pdf"])
paper_text = ""

if uploaded:
    st.success("Paper uploaded successfully")
    
    # Extract text from PDF
    pdf_reader = PyPDF2.PdfReader(uploaded)
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            paper_text += page_text + "\n"

    # Show a preview
    st.subheader("Paper Preview (first 1000 characters)")
    st.text(paper_text[:1000] + "...\n")

    # Summarize button
    if st.button("Summarize Paper"):
        with st.spinner("Summarizing..."):
            summary = summarize(paper_text)
            st.subheader("Summary")
            st.write(summary)

# --- CSV Search ---
topic = st.text_input("Search topic in dataset")
if topic:
    df_path = os.path.join(os.path.dirname(__file__), "../data/arxiv_processed.csv")
    if os.path.exists(df_path):
        df = pd.read_csv(df_path)
        results = df[df["title"].str.contains(topic, case=False, na=False)]
        st.subheader(f"Search Results for '{topic}'")
        st.write(results.head())
    else:
        st.warning(f"CSV file not found at {df_path}")