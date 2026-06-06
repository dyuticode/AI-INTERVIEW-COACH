# app.py
import streamlit as st
import os
from pathlib import Path
from dotenv import load_dotenv

# Find the exact folder where app.py lives, then look for the .env file there
env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)

# NOW YOUR OTHER IMPORTS CONTINUE BELOW...
from interview_questions import get_questions_by_type
from speech_utils import transcribe_speech
from feedback_engine import get_ai_feedback, generate_final_report

# Initialize Session States to keep track of interview progress
if "interview_started" not in st.session_state:
    st.session_state.interview_started = False
if "questions" not in st.session_state:
    st.session_state.questions = []
if "current_index" not in st.session_state:
    st.session_state.current_index = 0
if "history" not in st.session_state:
    st.session_state.history = []
if "interview_completed" not in st.session_state:
    st.session_state.interview_completed = False

st.set_page_config(page_title="AI Interview Coach", page_icon="🤖", layout="wide")

st.title("🤖 AI Interview Coach")
st.caption("Perfect your interviewing skills with real-time AI feedback and speech-to-text integration.")
st.markdown("---")

# Safety Check for API Key
if not os.environ.get("GEMINI_API_KEY"):
    st.warning("⚠️ `GEMINI_API_KEY` environment variable not found. Please set it to enable AI feedback.")

# --- SIDEBAR / SETUP ---
if not st.session_state.interview_started:
    st.subheader("Setup Your Interview Session")
    interview_type = st.selectbox("Choose Interview Type:", ["Technical Interview", "HR Interview"])
    
    if st.button("Start Interview 🚀"):
        st.session_state.questions = get_questions_by_type(interview_type)
        st.session_state.current_index = 0
        st.session_state.history = []
        st.session_state.interview_started = True
        st.session_state.interview_completed = False
        st.rerun()

# --- ACTIVE INTERVIEW INTERFACE ---
elif st.session_state.interview_started and not st.session_state.interview_completed:
    idx = st.session_state.current_index
    questions = st.session_state.questions
    
    # 1. Check if questions exist BEFORE attempting to display the active UI block
    if len(questions) > 0:
        # Progress Bar
        progress = (idx) / len(questions)
        st.progress(progress, text=f"Question {idx + 1} of {len(questions)}")
        
        st.info(f"**Question:** {questions[idx]}")
        
        # Input Mode Selection
        input_mode = st.radio("How would you like to answer?", ["Type Response", "Voice Input (Microphone)"], horizontal=True)
        
        user_answer = ""
        
        if input_mode == "Type Response":
            user_answer = st.text_area("Your Answer:", placeholder="Type your response here...", height=150)
            
        else:
            st.write("Click 'Record' and speak into your microphone. Wait for recording to complete.")
            if st.button("🎙️ Record Answer"):
                with st.spinner("Listening... Speak now."):
                    text, error = transcribe_speech()
                    if error:
                        st.error(error)
                    else:
                        st.session_state[f"voice_ans_{idx}"] = text
                        
            # If text was recorded, display it in a text area so user can review/edit it
            if f"voice_ans_{idx}" in st.session_state:
                user_answer = st.text_area("Transcribed Answer (Feel free to edit):", value=st.session_state[f"voice_ans_{idx}"], height=150)

        # Submit Button
        if st.button("Submit Answer & Get Feedback ➡️"):
            if not user_answer.strip():
                st.warning("Please provide an answer before submitting.")
            else:
                with st.spinner("AI is analyzing your answer..."):
                    feedback, error = get_ai_feedback(questions[idx], user_answer)
                    if error:
                        st.error(error)
                    else:
                        # Save question, answer, and feedback to history
                        st.session_state.history.append({
                            "question": questions[idx],
                            "answer": user_answer,
                            "feedback": feedback
                        })
                        
                        # Advance to next question or complete interview
                        if idx + 1 < len(questions):
                            st.session_state.current_index += 1
                        else:
                            st.session_state.interview_completed = True
                        st.rerun()
    else:
        # 2. Elegant exit fallback if your data loading fails or interview_questions.py is empty
        st.error("No questions found. Please check your `interview_questions.py` file configuration.")
        if st.button("⬅️ Back to Setup"):
            st.session_state.interview_started = False
            st.rerun()

    # Show live instant feedback of the PREVIOUS question if available
    if len(st.session_state.history) > 0:
        st.markdown("---")
        st.subheader("💡 Latest AI Feedback")
        last_entry = st.session_state.history[-1]
        st.markdown(f"**Q:** {last_entry['question']}")
        
        col1, col2 = st.columns([1, 4])
        with col1:
            st.metric(label="Score", value=f"{last_entry['feedback']['score']}/10")
        with col2:
            st.success(f"**Strengths:** {last_entry['feedback']['strengths']}")
            st.warning(f"**Weaknesses:** {last_entry['feedback']['weaknesses']}")
            st.info(f"**Suggested Better Answer:** {last_entry['feedback']['suggested_better_answer']}")

# --- FINAL REPORT INTERFACE ---
elif st.session_state.interview_completed:
    st.header("🏆 Interview Completed! Here is your Report")
    
    with st.spinner("Generating overall summary report..."):
        report, error = generate_final_report(st.session_state.history)
        
        if error:
            st.error(error)
        else:
            col1, col2 = st.columns([1, 3])
            with col1:
                st.metric(label="Overall Performance Score", value=f"{report['overall_score']}/10")
            with col2:
                st.subheader("Key Areas of Improvement")
                st.write(report['key_improvements'])
                
                st.subheader("Coach Summary")
                st.write(report['summary'])
                
    st.markdown("---")
    st.subheader("📋 Detailed Breakdown")
    
    for i, entry in enumerate(st.session_state.history):
        with st.expander(f"Question {i+1}: {entry['question'][:50]}..."):
            st.markdown(f"**Full Question:** {entry['question']}")
            st.markdown(f"**Your Answer:** {entry['answer']}")
            st.markdown(f"**Score:** {entry['feedback']['score']}/10")
            st.markdown(f"**Strengths:** {entry['feedback']['strengths']}")
            st.markdown(f"**Weaknesses:** {entry['feedback']['weaknesses']}")
            st.markdown(f"**Suggested Answer:** {entry['feedback']['suggested_better_answer']}")
            
    if st.button("Start a New Interview 🔄"):
        st.session_state.interview_started = False
        st.session_state.interview_completed = False
        st.rerun()