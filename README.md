# 🤖 AI Interview Coach

AI Interview Coach is a functional, real-time responsive web application designed to help job applicants practice and perfect their interviewing skills. Built as a comprehensive Phase 1 prototype, this application leverages Large Language Models (LLMs), natural language processing, and speech processing to deliver instantaneous, structured feedback on both **Technical** and **HR** interview paths.

## 🚀 Core Features

* **Dual-Track Simulation:** Dedicated question sets tailored specifically for Data Science, AI, Python engineering, and standard behavioral HR categories.
* **Multimodal Input Support:** Candidates have the choice to type out comprehensive text responses or speak naturally using microphone integration.
* **Real-time AI Evaluation:** Utilizes the Google Gemini API (`gemini-2.5-flash`) to instantly analyze answers for linguistic depth, correctness, and presentation.
* **Structured JSON Analytics:** The feedback engine enforces strict schema output to parse out exact metrics:
    * *Score (1-10)*
    * *Identified Strengths*
    * *Constructive Weaknesses*
    * *Suggested Better (Model) Answer*
* **Comprehensive Final Report:** Generates an end-of-session dashboard displaying an overall performance score, key areas of improvement, and an expandable question-by-question historical breakdown.



## 🏗️ System Architecture & File Structure

The project is engineered with a modular separation of concerns, decoupling the frontend interface from the audio abstraction layer and AI evaluation prompt architecture.


AI-Interview-Coach:

├── app.py                  # Main orchestration engine & Streamlit Web UI

├── interview_questions.py  # Static repository of curated Technical & HR question banks

├── feedback_engine.py      # Google Gemini API integration and structured JSON layout parser

├── speech_utils.py         # Audio capture and Speech-to-Text translation pipeline

├── requirements.txt        # Managed third-party dependencies package manifest

└── .env                    # Secure local environment configuration (Git-ignored)






