import streamlit as st
from interview_logic import generate_question, evaluate_answer
from utils import get_spoken_text
from roles import roles
import pandas as pd
import os
import re

st.set_page_config(page_title="AI Interview Simulator", layout="centered")

st.markdown("## 🎤 AI Interview Simulator")
st.markdown("Simulates an interview for various tech roles using GPT-3.5 and speech-to-text.")

# Candidate name input
candidate_name = st.text_input("👤 Enter your name:")
if not candidate_name:
    st.warning("Please enter your name to begin.")
    st.stop()

# Initialize session state variables
if "role" not in st.session_state:
    st.session_state.role = None
if "mode" not in st.session_state:
    st.session_state.mode = "Type"
if "asked" not in st.session_state:
    st.session_state.asked = []
if "current_question" not in st.session_state:
    st.session_state.current_question = None
    st.session_state.current_topic = None
if "spoken_answer" not in st.session_state:
    st.session_state.spoken_answer = ""

# Role selection
role = st.selectbox("🎯 Choose your interview role:", list(roles.keys()))
st.session_state.role = role

# Input mode selection
mode = st.radio("💬 Answer Input Mode:", ["Type", "Speak"], index=0)
st.session_state.mode = mode

# Generate first question if none yet
if not st.session_state.current_question:
    question, topic = generate_question(role, st.session_state.asked)
    st.session_state.current_question = question
    st.session_state.current_topic = topic

question = st.session_state.current_question
topic = st.session_state.current_topic

st.markdown(f"### ❓ {question}")

# Answer input area
answer = ""
if mode == "Type":
    answer = st.text_area("✍️ Type your answer below:", value=st.session_state.spoken_answer)
elif mode == "Speak":
    if st.button("🎙️ Start Recording"):
        spoken = get_spoken_text()
        if spoken:
            st.session_state.spoken_answer = spoken
            st.success("Transcribed Answer:")
            st.write(spoken)
        else:
            st.error("Could not understand. Try again.")
    answer = st.session_state.spoken_answer

# Helper function to extract rating from GPT feedback
def extract_rating(feedback_text):
    match = re.search(r'\b([1-9]|10)\b', feedback_text)
    if match:
        return int(match.group(0))
    return None

# Evaluate answer and save to CSV
if answer and st.button("📊 Evaluate Answer"):
    feedback = evaluate_answer(question, answer)
    st.subheader("📋 Feedback:")
    st.markdown(feedback)

    rating = extract_rating(feedback)
    if rating is None:
        rating = "N/A"

    # Save result
    result = {
        "Name": candidate_name,
        "Role": role,
        "Topic": topic,
        "Question": question,
        "Answer": answer,
        "Feedback": feedback,
        "Rating": rating
    }
    df = pd.DataFrame([result])

    if not os.path.exists("interview_results.csv"):
        df.to_csv("interview_results.csv", index=False)
    else:
        df.to_csv("interview_results.csv", mode="a", index=False, header=False)

    st.success("✅ Answer, feedback, and rating saved!")

# Button for next question
if st.button("➡️ Next Question"):
    if st.session_state.current_topic not in st.session_state.asked:
        st.session_state.asked.append(st.session_state.current_topic)
    question, topic = generate_question(role, st.session_state.asked)
    st.session_state.current_question = question
    st.session_state.current_topic = topic
    st.session_state.spoken_answer = ""
    st.rerun()

# Button to restart interview
if st.button("🔁 Restart Interview"):
    st.session_state.clear()
    st.rerun()
