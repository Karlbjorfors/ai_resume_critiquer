from token import OP
import streamlit as st
import os
from dotenv import load_dotenv

from resume_processor import extract_text_from_file, validate_file_content
from ai_analyzer import ResumeAnalyser

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="centered")


# Initialize the AI Resume Analyser
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
analyser = ResumeAnalyser(OPENAI_API_KEY)

# UI components
st.title("AI Resume Analyzer")
st.markdown("Upload your resume and get AI-powered feedback tailored to your needs!")

# File uploader and job role input
uploaded_file = st.file_uploader("Upload your resume (PDF or TXT).", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role you're applying too (optional)")

analyze = st.button("Analyze Resume")

# Main logic
if analyze and uploaded_file:
    try:
        # Extract text from the uploaded file
        file_content = extract_text_from_file(uploaded_file)

        # Validate the extracted content    
        if not validate_file_content(file_content):
            st.error("File does not have any content...")
            st.stop()

        # Analyze the resume content
        with st.spinner("Analyzing your resume..."):
            analysis_result = analyser.analyze_resume(file_content, job_role)

        # Display the analysis result
        st.markdown("### Analysis Results")
        st.markdown(analysis_result)

    except Exception as e:
        st.error(f"An error occured: {str(e)}")