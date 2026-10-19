# Project Report: StudyMate AI

## 1. Abstract
StudyMate AI is a web-based study assistant that uses Generative AI to help students understand topics, revise notes, and practice for examinations. It generates explanations, structured summaries, and quizzes from a topic or user-provided notes.

## 2. Problem Statement
Students often spend time turning long notes into revision material and may find difficult topics hard to understand. StudyMate AI provides a single interface for these study tasks.

## 3. Objectives
- Explain academic topics in simple language.
- Summarize pasted study notes.
- Generate practice questions with an answer key.
- Provide a simple and accessible user interface.

## 4. Technologies Used
- Python: application logic
- Streamlit: web interface
- Google Gemini API: generative AI
- python-dotenv: secure local environment configuration

## 5. Working
1. The user selects a task.
2. The user enters a topic and/or pastes notes.
3. The app builds a task-specific prompt.
4. The prompt is sent to the Gemini model.
5. The generated response is displayed on the page.

## 6. Main Features
- Topic explanation
- Notes summarization
- Quiz generation
- Study-level selection
- Input validation and basic error handling

## 7. Limitations
The app requires internet access and a valid API key. AI output may be inaccurate, so users should verify facts with reliable learning material.

## 8. Future Scope
- Downloadable revision notes
- Saved quiz history
- Subject-wise organization
- Support for uploaded PDF notes

## 9. Conclusion
StudyMate AI demonstrates how Generative AI can make common study tasks faster and more interactive through a simple web application.
