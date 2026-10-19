import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()
st.set_page_config(page_title="StudyMate AI", page_icon="📚", layout="centered")
st.title("📚 StudyMate AI")
st.caption("An AI study assistant that explains topics, summarizes notes, and creates practice quizzes.")

api_key = os.getenv("GEMINI_API_KEY", "")
if not api_key:
    st.warning("Add your Gemini API key to a .env file. See README.md for instructions.")
    st.stop()

client = genai.Client(api_key=api_key)

mode = st.selectbox("What would you like to do?", [
    "Explain a topic", "Summarize notes", "Create a practice quiz"
])
level = st.selectbox("Study level", ["School", "Diploma", "B.Tech / Undergraduate", "Beginner"])
topic = st.text_input("Topic or subject", placeholder="e.g., CPU scheduling, photosynthesis")
notes = st.text_area("Paste your notes (optional for topic explanation)", height=180)

if st.button("Generate", type="primary"):
    if not topic.strip() and not notes.strip():
        st.error("Please enter a topic or paste some notes.")
    else:
        if mode == "Explain a topic":
            prompt = f"""You are a friendly tutor. Explain '{topic}' for a {level} student using simple language.
Use headings, a relatable example, key terms, and a short recap. If notes are provided, use them as context:
{notes}"""
        elif mode == "Summarize notes":
            prompt = f"""Summarize the following study notes for a {level} student.
Include: short overview, 5-8 key points, important definitions, and a quick revision section.
Topic: {topic}
Notes:
{notes}"""
        else:
            prompt = f"""Create 8 practice questions about '{topic}' for a {level} student.
Use a mix of multiple-choice and short-answer questions. Put the answer key at the end, separated under
'Answer Key'. If notes are provided, base the quiz on them:
{notes}"""
        with st.spinner("StudyMate is preparing your material..."):
            try:
                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt
                )
                st.markdown(response.text or "No response returned. Please try again.")
            except Exception as exc:
                st.error(f"Could not generate a response: {exc}")
                st.info("Check your internet connection, API key, and available API quota.")
st.divider()
st.caption("Note: AI-generated study material can contain mistakes. Verify important facts with your textbook.")
