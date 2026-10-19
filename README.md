# StudyMate AI

A GenAI-powered study helper for students. It can explain a topic, summarize notes, and generate practice quizzes.

## Requirements
- Python 3.10 or newer
- Internet connection
- Gemini API key

## Run
1. Extract this folder.
2. Open a terminal in this folder.
3. Create a virtual environment (optional but recommended):
   - Windows: `python -m venv .venv` then `.venv\Scripts\activate`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
4. Install packages: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and add your Gemini API key.
6. Run: `streamlit run app.py`

Keep your API key private. Do not upload `.env` to a public repository.
