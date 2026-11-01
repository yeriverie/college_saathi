import json
import os
import streamlit as st

# Set page layout
st.set_page_config(
    page_title="College Saathi AI",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS for modern dark theme styling without emojis
st.markdown(
    """
    <style>
    .main {
        background-color: #0e1117;
        font-family: 'Inter', sans-serif;
    }
    .header-box {
        background: linear-gradient(135deg, #1e2640 0%, #0f172a 100%);
        padding: 24px;
        border-radius: 12px;
        border: 1px solid #334155;
        margin-bottom: 25px;
    }
    .header-title {
        color: #ffffff;
        font-size: 26px;
        font-weight: 700;
        margin: 0;
    }
    .header-subtitle {
        color: #94a3b8;
        font-size: 15px;
        margin-top: 5px;
    }
    .badge {
        display: inline-block;
        background-color: #2563eb;
        color: #ffffff;
        font-size: 11px;
        font-weight: 600;
        padding: 3px 8px;
        border-radius: 9999px;
        margin-top: 10px;
        text-transform: uppercase;
    }
    .exam-card {
        background-color: #1e293b;
        border-left: 4px solid #3b82f6;
        padding: 18px;
        border-radius: 8px;
        margin-bottom: 15px;
        border-top: 1px solid #334155;
        border-right: 1px solid #334155;
        border-bottom: 1px solid #334155;
    }
    .exam-title {
        color: #60a5fa;
        font-size: 17px;
        font-weight: 600;
        margin-bottom: 8px;
    }
    .exam-detail {
        color: #e2e8f0;
        font-size: 14px;
        margin: 4px 0;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- App Header ---
st.markdown(
    """
    <div class="header-box">
        <div class="header-title">College Saathi AI</div>
        <div class="header-subtitle">PDA College of Engineering, Kalaburagi</div>
        <span class="badge">Hackathon Prototype Demo | Live 5th Sem AI & ML</span>
    </div>
""",
    unsafe_allow_html=True,
)

# --- Load Data Safely ---
dir_name = os.path.abspath(os.path.dirname(__file__))
data_folder = os.path.join(dir_name, "data")
exams_path = os.path.join(data_folder, "exams.json")

exam_data = {"exams": []}
if os.path.exists(exams_path):
  try:
    with open(exams_path, "r", encoding="utf-8") as f:
      exam_data = json.load(f)
  except Exception:
    exam_data = {"exams": []}

# --- Search Input ---
user_query = st.text_input(
    "Search 5th Sem CIE-1 Schedule",
    placeholder="Type 'DBMS', 'ML', 'Data Science', '22AI51', or 'HCI'...",
)

# --- Search Logic ---
if user_query:
  matched_responses = []
  query_lower = user_query.strip().lower()

  acronym_map = {
      "dbms": "database management system",
      "ml": "machine learning",
      "ds": "data science",
      "hci": "human computer interface",
      "rm": "research methodology",
      "ipr": "ipr",
      "es": "environmental",
      "env": "environmental",
  }

  search_terms = [query_lower]
  if query_lower in acronym_map:
    search_terms.append(acronym_map[query_lower])

  for exam in exam_data.get("exams", []):
    subject_lower = exam["subject"].lower()
    code_lower = exam["code"].lower()

    is_match = False
    for term in search_terms:
      if (
          term in subject_lower
          or term in code_lower
          or any(w in subject_lower for w in term.split())
      ):
        is_match = True
        break

    if is_match:
      card_html = f"""
        <div class="exam-card">
            <div class="exam-title">Exam Found ({exam['semester']})</div>
            <div class="exam-detail"><strong>Subject:</strong> {exam['subject']} ({exam['code']})</div>
            <div class="exam-detail"><strong>Date:</strong> {exam['date']}</div>
            <div class="exam-detail"><strong>Session:</strong> {exam['session']}</div>
        </div>
        """
      if card_html not in matched_responses:
        matched_responses.append(card_html)

  st.markdown(
      "**[College Saathi AI]:**",
  )
  if matched_responses:
    for resp in matched_responses:
      st.markdown(resp, unsafe_allow_html=True)
  else:
    st.error(
        f"No matching record found for '{user_query}'. Try searching for"
        " 'DBMS', 'ML', 'Data Science', or 'HCI'."
    )
    
