import streamlit as st
from llm_helper import ask_gemini

st.set_page_config(
    page_title="AI Job Description Analyzer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Job Description Analyzer")

st.write(
    "Paste a Job Description below and let AI analyze it using Gemini."
)

job_description = st.text_area(
    "Paste Job Description",
    height=300,
    placeholder="Paste your job description here..."
)

if st.button("Analyze JD"):

    if job_description.strip() == "":
        st.warning("Please paste a Job Description.")
    else:

        with st.spinner("Analyzing..."):

            prompt = f"""
Analyze the following Job Description.

Return the response in the following format:

## Required Technical Skills

## Required Soft Skills

## Experience Required

## Interview Questions

## Learning Roadmap

Job Description:

{job_description}
"""

            result = ask_gemini(prompt)

        st.success("Analysis Complete!")

        st.markdown(result)