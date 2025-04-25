# GR5243_Project_3
A simple Streamlit app to run a 2×2 factorial A/B experiment testing how tone and framing affect user reasoning and feedback.

Deployed website link: [https://johnfeng2023-gr5243-project-3-app-i4mcwt.streamlit.app](https://johnfeng2023-gr5243-project-3-app-i4mcwt.streamlit.app)

## Research Overview

- **Design**: 2×2 between-subjects A/B experiment
- **Independent Variables**:
  - Greeting Style: **Formal** vs. **Friendly**
  - Task Framing: **Academic** vs. **Fun**
- **Outcome Measures**:
  - Number of correct answers (performance)
  - Time taken to complete the quiz (engagement)
  - Likert-scale feedback (subjective experience)

## Tech Stack

- [Streamlit](https://streamlit.io) for the frontend
- Python for logic and data handling
- Google Sheets API for storing participant results
- Google Analtyics for tracking background event

## How to Run the App

1. Clone the Repository
```
git clone https://github.com/johnfeng2023/GR5243_Project_3.git
cd GR5243_Project_3
```

2. Set Up Virtual Environment
```
python -m venv venv
source venv/bin/activate
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Run the Streamlit App
```
streamlit run app.py
```
