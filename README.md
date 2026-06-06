# 🤖 AI Interview Coach

A functional, real-time responsive web application designed to help job applicants practice for Technical and HR interviews using Large Language Models (LLMs) and Speech Processing.

## 🚀 Features
* **Dual Tracks:** Custom interview pools for Technical and HR tracks.
* **Multimodal Inputs:** Answer questions via text input or audio transcription using Speech Recognition.
* **Real-time Evaluation:** Uses Google Gemini (`gemini-2.5-flash`) to deliver instantaneous scoring, feedback on strengths, weaknesses, and alternative model answers.
* **Comprehensive Metrics:** Generates a complete end-of-session performance report.

## 🛠️ Tech Stack
* **Frontend:** Streamlit
* **AI Model:** Google Gemini API (`google-genai`)
* **Audio Processing:** SpeechRecognition & PyAudio

## ⚙️ Setup Instructions
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file in the root directory and add your key:
   `GEMINI_API_KEY=your_key_here`
4. Run the app: `streamlit run app.py`
