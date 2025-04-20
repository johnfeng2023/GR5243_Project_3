
import streamlit as st
import time
import random

# Show friendly-only bottom-right illustration
import base64
<<<<<<< HEAD
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

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

=======
>>>>>>> ivy-update

def get_image_base64(file_path):
    with open(file_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()



# Page config
st.set_page_config(page_title="Quiz", layout="centered")

<<<<<<< HEAD
import streamlit.components.v1 as components

components.html("""
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-8QCB98258G"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  // Main page view event
  gtag('config', 'G-8QCB98258G', {
    'page_title': 'Streamlit Quiz App',
    'page_path': window.location.pathname
  });
</script>
""", height=0)

=======
>>>>>>> ivy-update

# Gradient background fallback with improved layout (for "Friendly")
page_bg = """
<style>
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(to bottom right, #fef6fb, #e0f7fa) !important;
    }
    [data-testid="stHeader"] {
        background: rgba(0, 0, 0, 0);
    }
</style>
"""



TRICKY_QUESTIONS = [
    # 📘 Common Knowledge + Distractor (10)
    {"question": "Which of these is a mammal?", "options": ["Frog", "Shark", "Dolphin"], "answer": "Dolphin"},
    {"question": "What is the square root of 144?", "options": ["12", "14", "16"], "answer": "12"},
    {"question": "Which planet is known for its rings?", "options": ["Mars", "Saturn", "Venus"], "answer": "Saturn"},
    {"question": "Which animal lays eggs?", "options": ["Bat", "Whale", "Platypus"], "answer": "Platypus"},
    {"question": "Which sentence is grammatically correct?", "options": ["He don't know", "He doesn't know", "He not know"], "answer": "He doesn't know"},
    {"question": "Which is the largest continent?", "options": ["Africa", "Asia", "Europe"], "answer": "Asia"},
    {"question": "Which is a renewable energy source?", "options": ["Coal", "Wind", "Oil"], "answer": "Wind"},
    {"question": "Which food is highest in protein?", "options": ["Apple", "Chicken breast", "Carrot"], "answer": "Chicken breast"},
    {"question": "Which number is a multiple of both 3 and 5?", "options": ["10", "15", "20"], "answer": "15"},
    {"question": "What color is the sun most likely at noon?", "options": ["White", "Yellow", "Red"], "answer": "White"},
    
    # 🎯 Attention Checks (3)
<<<<<<< HEAD
    {"question": "Which road sign indicates a school zone?", "options": ["Sign A", "Sign B", "Sign C"], "answer": "Sign B", "image": True},
=======
    {"question": "Which of the following is spelled incorrectly?", "options": ["Accommodate", "Definately", "Occasionally", "Recommend"], "answer": "Definately"}

>>>>>>> ivy-update

    # 🔢 Math + Visual/Diagram Reasoning (10)
    {"question": "A triangle has sides 5, 5, and 6. Which angle is largest?", "options": ["Angle A", "Angle B", "Angle C"], "answer": "Angle C", "explain": True},
    {"question": "What comes next in the sequence: 3, 6, 12, 24, ...?", "options": ["36", "48", "30"], "answer": "48"},
    {"question": "You flip a fair coin 3 times. What is the probability of getting exactly two heads?", "options": ["1/4", "3/8", "1/2"], "answer": "3/8", "explain": True},
    {"question": "How many squares are in a 3x3 grid?", "options": ["9", "14", "15"], "answer": "14", "explain": True},
    {"question": "A triangle has sides 3, 4, 5. What type is it?", "options": ["Equilateral", "Right-angled", "Scalene"], "answer": "Right-angled", "explain": True},
    {"question": "A clock shows 3:15. What angle is between the hour and minute hand?", "options": ["7.5°", "45°", "90°"], "answer": "7.5°", "explain": True},
    {"question": "Which number does NOT belong in the set: 2, 4, 6, 9, 10?", "options": ["4", "9", "10"], "answer": "9"},
    {"question": "Which pattern comes next: ▲ ● ▲ ● ▲ ?", "options": ["▲", "●", "■"], "answer": "●"},
    {"question": "A square rotates 90° clockwise each time. If the first image shows ▲ at the top, what will be at the top after 3 rotations?", "options": ["▲", "▶", "▼"], "answer": "▼", "explain": True},
    {"question": "Which direction is the shadow pointing if the sun is in the east?", "options": ["West", "North", "East"], "answer": "West"},
    
    # 🎯 Attention Checks (3)
<<<<<<< HEAD
    {"question": "Which of these figures will complete the symmetry?", "options": ["Figure A", "Figure B", "Figure C"], "answer": "Figure A", "image": True},
=======
    {"question": "Choose the **second** number that is a multiple of 3.", "options": ["4", "6", "9", "11"], "answer": "9"}

>>>>>>> ivy-update

    # 🔍 Logical Reasoning (7)
    {"question": "If all Bloops are Razzies and all Razzies are Lazzies, are all Bloops Lazzies?", "options": ["Yes", "No", "Can't tell"], "answer": "Yes", "explain": True},
    {"question": "You walk 10 km north, then 10 km east. Where are you relative to the starting point?", "options": ["Northeast", "Southeast", "Northwest"], "answer": "Northeast"},
    {"question": "You see a boat full of people but there isn’t a single person on board. How?", "options": ["It's underwater", "They're all married", "It's a ghost ship"], "answer": "They're all married"},
    {"question": "All roses are flowers. Some flowers fade quickly. Can we conclude that some roses fade quickly?", "options": ["Yes", "No", "Can't tell"], "answer": "Can't tell", "explain": True},
    {"question": "If it rains, the ground gets wet. The ground is wet. What can we conclude?", "options": ["It must have rained", "It might have rained", "It didn’t rain"], "answer": "It might have rained", "explain": True},
    {"question": "Anna is older than Bella. Bella is older than Carla. Who is the oldest?", "options": ["Anna", "Bella", "Carla"], "answer": "Anna"},
    {"question": "A man has 4 sons. Each son has a sister. How many children does he have?", "options": ["5", "8", "9"], "answer": "5"},

    # 🎯 Attention Checks (3)
<<<<<<< HEAD
    {"question": "In the grid, which path reaches the goal with the fewest turns?", "options": ["Path A", "Path B", "Path C"], "answer": "Path C", "image": True}
=======
    {"question": "If the third option is 'True', select the first. Otherwise, select the fourth.", "options": ["Option A", "Option B", "True", "Option D"], "answer": "Option A"}
>>>>>>> ivy-update
]

LIKERT_QUESTIONS = [
    # SDT
    "I was motivated to answer the quiz questions carefully.",
    "The tone of the quiz made me feel more engaged.",
    "I felt a sense of autonomy while completing the quiz.",
    "I tried to do my best because I found the tone encouraging.",
    # CLT
    "The interface helped me stay focused throughout the quiz.",
    "I was distracted by unnecessary elements in the interface. ",
    "The visual design made it easier to understand the questions.",
    "I spent extra effort navigating or interpreting the interface. ",
    # Overall Assessment
    "I took the quiz seriously and gave thoughtful answers.",
    "I believe my responses reflect my actual knowledge and understanding.",
]

# Session initialization
if "page" not in st.session_state:
    st.session_state.page = "welcome"
    st.session_state.style = random.choice(["A", "B"])  
    st.session_state.question_index = 0
    st.session_state.answers = []
    st.session_state.correct_count = 0
    st.session_state.likert_index = 0
    st.session_state.likert_responses = []
    random.seed() 
    # randomly select 15 out of 30
    st.session_state.shuffled_questions = random.sample(TRICKY_QUESTIONS, 15)

# Only apply gradient background if Friendly style ("A")
if "style" in st.session_state and st.session_state.style == "A":
    st.markdown(page_bg, unsafe_allow_html=True)


# Welcome page
def render_intro():
    if st.session_state.style == "A":
        st.markdown("<h1 style='text-align:center;color:#d63384;'>🌈 Welcome to the Quiz 🌈</h1>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align:center;'> This is a lighthearted quiz – see how many you can answer!</h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align:center;'> Some questions are simple, some might be a bit tricky 😄 </h4>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align:center;'> No pressure at all – just try your best and have fun! ✨ </h4>", unsafe_allow_html=True)
    else:
        st.markdown("<h1 style='text-align:center;color:#333;'>Welcome to the Survey</h1>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align:center;'> This is a short questionnaire designed to assess your responses. </h5>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align:center;'> Some items may be straightforward, while others may require more thought. </h5>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align:center;'> Please read each question carefully and answer to the best of your ability. </h5>", unsafe_allow_html=True)


# Then in your main welcome page:
if st.session_state.page == "welcome":

    render_intro()
    if st.button("Start Quiz"):
        st.session_state.page = "quiz"
        st.session_state.start_time = time.time()
<<<<<<< HEAD
        components.html(f"""
        <script>
        gtag('event', 'start_quiz', {{
            'style': '{st.session_state.style}'
        }});
        </script>
        """, height=0)
=======
>>>>>>> ivy-update


# Quiz page
elif st.session_state.page == "quiz":
    i = st.session_state.question_index
    q = st.session_state.shuffled_questions[i]


    card_style = """
    background-color:#ffffffdd;
    padding:20px 30px;
    border-radius:15px;
    margin-bottom:20px;
    """
    if st.session_state.style == "A":
        card_style += "box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.08), 0px 8px 24px rgba(0, 0, 0, 0.08);"
    
    st.markdown(f"""
    <div style="{card_style}">
        <h3 style='color:#d63384;'>🧠 Question {i+1} of 15</h3>
        <p style='font-size:20px; font-weight:600;'>💡 {q["question"]}</p>
    </div>
    """, unsafe_allow_html=True)




    # 仅在 Friendly 风格下显示插图
    if st.session_state.style == "A":
        image_base64 = get_image_base64("01.png")

        st.markdown(
            f"""
            <div style='position: fixed; bottom: 120px; right: 40px; z-index: 9999;'>
                <img src="data:image/png;base64,{image_base64}" width="220" style="opacity: 0.92;">
            </div>
            """,
            unsafe_allow_html=True
        )  



    answer = st.radio(
        label="",
        options=["-- Select an answer --"] + q["options"],
        index=0
    )

    explanation = ""
    if q.get("explain"):
        explanation = st.text_input(
            "💬 Why do you think this is the right answer?",
            key=f"explain_{i}"
        )

<<<<<<< HEAD
=======

>>>>>>> ivy-update
    if st.button("Submit and Continue"):
        if answer == "-- Select an answer --" or (q.get("explain") and explanation.strip() == ""):
            st.warning("⚠️ Please complete the question before continuing.")
        else:
            st.session_state.answers.append((q["question"], answer, explanation))
            if answer == q["answer"]:
                st.session_state.correct_count += 1

<<<<<<< HEAD
            # Google Analytics event tracking for quiz answer
            components.html(f"""
            <script>
            gtag('event', 'submit_answer', {{
                question_number: {i+1},
                is_correct: {str(answer == q["answer"]).lower()},
                answer_text: '{answer}'
            }});
            </script>
            """, height=0)

=======
>>>>>>> ivy-update
            st.session_state.question_index += 1
            if st.session_state.question_index >= 15:
                st.session_state.page = "transition"

            st.rerun()

<<<<<<< HEAD

=======
>>>>>>> ivy-update
    progress = (i + 1) / 15
    # Friendly 风格：用 emoji 气泡进度条
    if st.session_state.style == "A":
        bar = "⭐️" * int(progress * 15) + "⚪️" * (15 - int(progress * 15))
        st.markdown(f"**Progress**: {bar} {int(progress * 100)}%")
    
    # Formal 风格：保留默认条形进度条
    else:
        st.progress(progress)


# Transition page between quiz and likert
elif st.session_state.page == "transition":
    if st.session_state.style == "A":
        st.snow()
        st.markdown("<h2 style='text-align:center;color:#d63384;'>🎉 You've completed the quiz!</h2>", unsafe_allow_html=True)
        st.markdown("Great job finishing the quiz! 🎯 ", unsafe_allow_html=True)
        
        # 添加按钮样式
        button_style = """
        <style>
        div.stButton > button:first-child {
            background-color: #ff4b4b;
            color: white;
            border-radius: 10px;
            height: 3em;
            width: 100%;
            font-size: 18px;
        }
        </style>
        """
        st.markdown(button_style, unsafe_allow_html=True)

        st.markdown("Now, please share your thoughts about the experience below. ✨", unsafe_allow_html=True)
        if st.button("Continue to Feedback"):
            st.session_state.page = "likert"
            st.rerun()

    else:
        st.markdown("<h2 style='text-align:center;'>Quiz section completed</h2>", unsafe_allow_html=True)
        st.write("Please proceed to answer a few questions about your experience with the quiz.")
        if st.button("Continue"):
            st.session_state.page = "likert"
            st.rerun()


# Likert scale page
elif st.session_state.page == "likert":
    j = st.session_state.likert_index
    likert_key = f"likert_{j}"

    # 只在第一次显示该题时初始化默认值
    if f"likert_{j}" not in st.session_state:
        st.session_state[f"likert_{j}"] = "— Select an answer —"

    #if st.session_state.style == "A":
        #st.markdown(f"<h3> 💭 How did you feel? ({j+1} of {len(LIKERT_QUESTIONS)})</h3>", unsafe_allow_html=True)
    #else:
        #st.markdown(f"<h3> Evaluation Item {j+1} of {len(LIKERT_QUESTIONS)}</h3>", unsafe_allow_html=True)
        #<h3 style='color:#d63384;'>🧠 Question {i+1} of 15</h3>

    #st.markdown(f"<div style='font-size: 20px; font-weight: 600; line-height:1.6'>{LIKERT_QUESTIONS[j]}</div>", unsafe_allow_html=True)

    # 插图只在 Friendly 风格下显示
    if st.session_state.style == "A":
        image_base64 = get_image_base64("02.png")  # 如果图像名是02.png，放在同一目录
        st.markdown(f"<h3 style='color:#d63384;'> 💭 How did you feel? ({j+1} of {len(LIKERT_QUESTIONS)})</h3>", unsafe_allow_html=True)

        # Show question + image side by side using flex
        st.markdown(f"""
        <div style='display: flex; justify-content: space-between; align-items: flex-start;'>
          <div style='flex: 1; padding-right: 20px;'>
            <div style='font-size: 20px; font-weight: 600; margin-bottom: 10px;'>{LIKERT_QUESTIONS[j]}</div>
          </div>
          <div style='flex-shrink: 0;'>
            <img src="data:image/png;base64,{image_base64}" width="240"/>
          </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"<h3>🧾 Evaluation Item {j+1} of {len(LIKERT_QUESTIONS)}</h3>", unsafe_allow_html=True)
        st.markdown(f"<div style='font-size: 20px; font-weight: 600; margin-bottom: 10px;'>{LIKERT_QUESTIONS[j]}</div>", unsafe_allow_html=True)


    likert_options = ["— Select an answer —", "Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"]
    response = st.radio("Please indicate your level of agreement:",
                    likert_options,
                    index=likert_options.index(st.session_state[f"likert_{j}"]),
                    key=f"likert_{j}")


    if st.button("Submit and Continue"):
        if response == "— Select an answer —":
            st.error('⚠️ Please select your response before continuing.')
        else:
            st.session_state.likert_responses.append((LIKERT_QUESTIONS[j], response))
<<<<<<< HEAD

            components.html(f"""
                    <script>
                    gtag('event', 'submit_likert_response', {{
                        question_number: {j+1},
                        question_text: '{LIKERT_QUESTIONS[j]}',
                        response: '{response}'
                    }});
                    </script>
                    """, height=0)

            st.session_state.likert_index += 1
=======
            st.session_state.likert_index += 1

>>>>>>> ivy-update
            if st.session_state.likert_index >= len(LIKERT_QUESTIONS):
                st.session_state.page = "result"
            st.rerun()

    progress = ((j + 1) / len(LIKERT_QUESTIONS))
    # Friendly 风格：用 emoji 气泡进度条
    if st.session_state.style == "A":
        bar = "⭐️" * int(progress * 15) + "⚪️" * (15 - int(progress * 15))
        st.markdown(f"**Progress**: {bar} {int(progress * 100)}%")
    
    # Formal 风格：保留默认条形进度条
    else:
        st.progress(progress)


# Result page
elif st.session_state.page == "result":
    st.balloons()
    st.success("🎉 Quiz Completed!")

<<<<<<< HEAD
    from datetime import datetime
    import pandas as pd

    if "submitted" not in st.session_state:
        duration = round(time.time() - st.session_state.start_time, 2)
        result = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "style": st.session_state.style,
            "correct_count": st.session_state.correct_count,
            "duration_sec": duration,
        }

        for i, (q, a, e) in enumerate(st.session_state.answers):
            result[f"Q{i+1}"] = a
            result[f"Q{i+1}_explanation"] = e

        for j, (q, s) in enumerate(st.session_state.likert_responses):
            result[f"Likert_{j+1}"] = s

        try:
            append_to_google_sheet(result)

            components.html(f"""
            <script>
            gtag('event', 'quiz_complete', {{
                correct_count: {st.session_state.correct_count},
                duration_sec: {duration},
                style: '{st.session_state.style}'
            }});
            </script>
            """, height=0)

            st.session_state.submitted = True
            st.success("📊 Results have been recorded to Google Sheets.")
        except Exception as e:
            st.error(f"❌ Failed to save results: {e}")



=======
>>>>>>> ivy-update
