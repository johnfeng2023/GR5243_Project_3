import streamlit as st
import time
import pandas as pd
from datetime import datetime
import streamlit.components.v1 as components
import random
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Analytics setup
components.html("""
<script async src="https://www.googletagmanager.com/gtag/js?id=G-8QCB98258G"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-8QCB98258G');
  gtag('event', 'page_view', {
    page_title: 'Streamlit Quiz App',
    page_path: window.location.pathname
  });
</script>
""", height=0)

def append_to_google_sheet(row_dict):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds_json = json.loads(st.secrets["gspread"]["gcp_service_account"])
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_json, scope)
    client = gspread.authorize(creds)
    sheet = client.open("Experiment Results").worksheet("responses")
    sheet.append_row(list(row_dict.values()))

st.set_page_config(page_title="Trivia Quiz", layout="centered")

# Background
page_bg_img = """
<style>
body {
background: linear-gradient(to bottom, #a1c4fd, #c2e9fb);
}
[data-testid="stAppViewContainer"] > .main {
background-color: rgba(255, 255, 255, 0.0);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

combinations = [("Formal", "Academic"), ("Formal", "Fun"),
                ("Friendly", "Academic"), ("Friendly", "Fun")]

if "assigned_group" not in st.session_state:
    st.session_state.assigned_group = random.choice(combinations)
    st.session_state.page = "welcome"
    st.session_state.answers = []
    st.session_state.correct_count = 0
    st.session_state.question_index = 0
    st.session_state.start_time = time.time()

greeting, framing = st.session_state.assigned_group

TRICKY_QUESTIONS = [
    {"question": "Which is heavier?",
     "options": ["1 kg of iron", "1 kg of cotton", "Same weight"], "answer": "Same weight"},
    {"question": "A farmer has 17 sheep, all but 9 run away. How many are left?",
     "options": ["0", "9", "8", "17"], "answer": "9"},
    {"question": "How many months have 28 days?",
     "options": ["1", "2", "12"], "answer": "12"},
    {"question": "Which number comes next: 2, 4, 8, 16, ...?",
     "options": ["32", "20", "24"], "answer": "32"},
    {"question": "You see a boat filled with people, yet there isn't a single person on board. How is that possible?",
     "options": ["They are invisible", "All are married", "It’s a ghost ship"], "answer": "All are married"}
]

if st.session_state.page == "welcome":
    if greeting == "Friendly":
        st.markdown("""
        <div style="background-color:#fff0f5; padding: 30px; border-radius: 15px;">
            <h1 style='color:#e75480; font-size:36px;'>🎉 Welcome, friend!</h1>
            <p style='font-size:20px;'>We're <strong>so happy</strong> you're here! 🥳</p>
            <p style='font-size:18px;'>This quiz is full of quirky questions to <span style="color:#fa8072;">tickle your brain</span> 🧠 and keep you smiling 😄.</p>
            <p style='font-size:16px;'>Take your best guess and have fun! 💡</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.title("Welcome to this research study.")
        st.write("This study aims to examine human reasoning strategies when processing different types of information in everyday contexts.")
        st.write("Your responses will help us better understand how question framing affects decision-making behavior.")
        st.write("Please answer as thoughtfully and honestly as you can. We sincerely appreciate your participation.")

    if st.button("Start Quiz"):
        st.session_state.page = "quiz"
        st.session_state.start_time = time.time()
        components.html("""
        <script>
          gtag('event', 'start_quiz', {
            event_category: 'engagement',
            event_label: 'User clicked start'
          });
        </script>
        """, height=0)

elif st.session_state.page == "quiz":
    i = st.session_state.question_index
    q = TRICKY_QUESTIONS[i]

    with st.container():
        st.markdown(f"<h3 style='color:#ff69b4;'>🧠 Question {i+1} of {len(TRICKY_QUESTIONS)}</h3>", unsafe_allow_html=True)
        user_answer = st.radio(f"💡 {q['question']}", q["options"], key=f"q{i}")
        explanation = st.text_input("💬 Why do you think this is the right answer?", key=f"e{i}")

        if st.button("Submit and Continue"):
            st.session_state.answers.append({
                "question": q["question"],
                "user_answer": user_answer,
                "is_correct": user_answer == q["answer"],
                "explanation": explanation
            })
            if user_answer == q["answer"]:
                st.session_state.correct_count += 1

            if i + 1 < len(TRICKY_QUESTIONS):
                st.session_state.question_index += 1
            else:
                st.session_state.page = "feedback"

elif st.session_state.page == "feedback":
    st.subheader("📝 Feedback")
    likert_questions = [
        "I found the task enjoyable.",
        "The tone of the message influenced my mood.",
        "I felt motivated to complete the quiz.",
        "The questions were challenging in a good way.",
        "I would participate in similar experiments again."
    ]
    likert_scores = {}
    for i, q in enumerate(likert_questions):
        likert_scores[q] = st.slider(q, 1, 5, 3, key=f"lq{i}")

    if st.button("Submit Feedback"):
        duration = round(time.time() - st.session_state.start_time, 2)
        result = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "greeting": greeting,
            "framing": framing,
            "correct_count": st.session_state.correct_count,
            "duration_sec": duration,
        }
        for i, a in enumerate(st.session_state.answers):
            result[f"Q{i+1}"] = a["user_answer"]
            result[f"Q{i+1}_explanation"] = a["explanation"]
        for q, s in likert_scores.items():
            result[q] = s

        append_to_google_sheet(result)

        components.html(f"""
        <script>
          gtag('event', 'submit_feedback', {{
            event_category: 'feedback',
            value: {duration},
            event_label: 'Feedback Submitted'
          }});

          gtag('event', 'session_duration', {{
            event_category: 'timing',
            value: {duration},
            event_label: 'Time on app (s)'
          }});
        </script>
        """, height=0)

        st.success("🎉 Thank you! Your responses have been saved.")
        st.balloons()
        st.session_state.page = "done"

elif st.session_state.page == "done":
    st.title("✅ Submission Complete")
    st.write("Thank you again for participating!")
