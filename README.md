# GR5243_Project_3
A simple Streamlit app to run a 2×2 factorial A/B experiment testing how tone and framing affect user reasoning and feedback.

Deployed website link: [https://gr5243project3-jjvfg5wlaxskz6xli8fguf.streamlit.app/](https://gr5243project3-jjvfg5wlaxskz6xli8fguf.streamlit.app/)

## 🧪 Research Overview

- **Design**: 2×2 between-subjects A/B experiment
- **Independent Variables**:
  - Greeting Style: **Formal** vs. **Friendly**
  - Task Framing: **Academic** vs. **Fun**
- **Outcome Measures**:
  - Number of correct answers (performance)
  - Time taken to complete the quiz (engagement)
  - Likert-scale feedback (subjective experience)

## 💻 Tech Stack

- [Streamlit](https://streamlit.io) for the frontend
- Python for logic and data handling
- Google Sheets API for storing participant results

## 🚀 Deployment Instructions (for Streamlit Cloud)

1. Fork or clone this repo
2. Set up a Google Sheet and enable the Sheets API
3. Add your API credentials to Streamlit secrets (`st.secrets`)
4. Deploy the app via [Streamlit Cloud](https://streamlit.io/cloud)
