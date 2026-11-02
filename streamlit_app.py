import json
import os
import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="College Saathi AI",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- Custom Styling (Dark Theme & Clean Chat Cards) ---
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
    .card {
        background-color: #1e293b;
        border-left: 4px solid #3b82f6;
        padding: 18px;
        border-radius: 8px;
        margin-bottom: 15px;
        border-top: 1px solid #334155;
        border-right: 1px solid #334155;
        border-bottom: 1px solid #334155;
    }
    .card-title {
        color: #60a5fa;
        font-size: 17px;
        font-weight: 600;
        margin-bottom: 8px;
    }
    .card-detail {
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
        <div class="header-subtitle">P.D.A. College of Engineering, Kalaburagi</div>
        <span class="badge">Autonomous Campus Assistant</span>
    </div>
""",
    unsafe_allow_html=True,
)

# --- Load Dataset Safely ---
dir_name = os.path.abspath(os.path.dirname(__file__))
data_folder = os.path.join(dir_name, "data")
json_path = os.path.join(data_folder, "campus_data.json")

default_data = {
    "institution": "P.D.A. College of Engineering",
    "website": "pdacek.ac.in",
    "portals": {
        "results": "https://pda-results.contineo.in/index.php",
        "general_webfiles": "https://pda-students.contineo.in/webfiles/",
        "terms": {
            "odd_semester": "https://pda-students.contineo.in/parents/",
            "even_semester": "https://pda-students.contineo.in/parentseven/index.php",
            "summer_term": (
                "https://pda-students.contineo.in/parentssummer/index.php"
            ),
        },
    },
    "exams": [
        {
            "semester": "V Semester AI & ML",
            "subject": "Data Science & Its Applications",
            "code": "22AI51",
            "date": "29/10/2026",
            "session": "11:30 AM to 12:45 PM",
        },
        {
            "semester": "V Semester AI & ML",
            "subject": "Database Management System",
            "code": "22AI52",
            "date": "29/10/2026",
            "session": "04:00 PM to 05:15 PM",
        },
        {
            "semester": "V Semester AI & ML",
            "subject": "Principles of Machine Learning",
            "code": "22AI53",
            "date": "30/10/2026",
            "session": "11:30 AM to 12:45 PM",
        },
        {
            "semester": "V Semester AI & ML",
            "subject": "Human Computer Interface",
            "code": "22AI55A",
            "date": "30/10/2026",
            "session": "04:00 PM to 05:15 PM",
        },
        {
            "semester": "V Semester AI & ML",
            "subject": "Research Methodology and IPR",
            "code": "22RM157",
            "date": "31/10/2026",
            "session": "11:30 AM to 12:45 PM",
        },
        {
            "semester": "V Semester AI & ML",
            "subject": "Environmental Studies",
            "code": "22ES58",
            "date": "31/10/2026",
            "session": "04:00 PM to 05:15 PM",
        },
    ],
    "fee_structure": {
        "kcet_fee_structure": [
            {
                "category": "KCET (Un-Aided Course)",
                "total_fee": 130956,
                "tuition_fee": 85346,
                "other_fee": 20000,
            },
            {
                "category": "KCET (Aided Course)",
                "total_fee": 67866,
                "tuition_fee": 22256,
                "other_fee": 20000,
            },
        ],
        "management_quota_fees_per_year": [
            {
                "course": "Computer Science Engineering",
                "fees_per_year": 250000,
            },
            {
                "course": (
                    "Artificial Intelligence and Machine Learning"
                ),
                "fees_per_year": 250000,
            },
            {"course": "Civil Engineering", "fees_per_year": 140000},
            {"course": "Mechanical Engineering", "fees_per_year": 140000},
        ],
        "comedk_fee_structure": [
            {
                "course": "Computer Science Engineering",
                "total_fee": 216610,
                "tuition_fee": 186000,
            },
            {
                "course": (
                    "Artificial Intelligence and Machine Learning"
                ),
                "total_fee": 216610,
                "tuition_fee": 186000,
            },
        ],
    },
}

campus_data = default_data
if os.path.exists(json_path):
  try:
    with open(json_path, "r", encoding="utf-8") as f:
      campus_data = json.load(f)
  except Exception:
    campus_data = default_data

# --- Real Chatbot Interface ---
st.markdown("### Ask College Saathi")
user_query = st.text_input(
    "Ask anything about exams, fees, or login links...",
    placeholder=(
        "Try typing 'AIML fee', 'CSE fee', 'DBMS exam', 'results', or 'odd sem"
        " login'..."
    ),
)

if user_query:
  query_lower = user_query.strip().lower()
  response_found = False

  st.markdown("**[College Saathi AI]:**")

  # 1. Check for Exams & Acronyms
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

  for exam in campus_data.get("exams", []):
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
      response_found = True
      st.markdown(
          f"""
            <div class="card">
                <div class="card-title">Exam Found ({exam['semester']})</div>
                <div class="card-detail"><strong>Subject:</strong> {exam['subject']} ({exam['code']})</div>
                <div class="card-detail"><strong>Date:</strong> {exam['date']}</div>
                <div class="card-detail"><strong>Session:</strong> {exam['session']}</div>
            </div>
            """,
          unsafe_allow_html=True,
      )

  # 2. Check for Fee Structure (AIML, CSE, Management, KCET, COMEDK)
  if "fee" in query_lower:
    response_found = True
    fees = campus_data.get("fee_structure", {})

    # Specific check for AIML or CSE
    if "aiml" in query_lower or "artificial intelligence" in query_lower:
      st.markdown(
          "**Fee details for Artificial Intelligence and Machine Learning:**"
      )
      for item in fees.get("management_quota_fees_per_year", []):
        if "Artificial Intelligence" in item["course"]:
          st.markdown(
              f"""
                    <div class="card">
                        <div class="card-title">Management Quota</div>
                        <div class="card-detail"><strong>Course:</strong> {item['course']}</div>
                        <div class="card-detail" style="color: #60a5fa;"><strong>Annual Fee:</strong> INR {item['fees_per_year']:,}</div>
                    </div>
                    """,
              unsafe_allow_html=True,
          )
      for item in fees.get("comedk_fee_structure", []):
        if "Artificial Intelligence" in item["course"]:
          st.markdown(
              f"""
                    <div class="card">
                        <div class="card-title">COMEDK Quota</div>
                        <div class="card-detail"><strong>Course:</strong> {item['course']}</div>
                        <div class="card-detail" style="color: #60a5fa;"><strong>Total Fee:</strong> INR {item['total_fee']:,}</div>
                    </div>
                    """,
              unsafe_allow_html=True,
          )

    elif "cse" in query_lower or "computer science" in query_lower:
      st.markdown("**Fee details for Computer Science Engineering:**")
      for item in fees.get("management_quota_fees_per_year", []):
        if "Computer Science Engineering" in item["course"]:
          st.markdown(
              f"""
                    <div class="card">
                        <div class="card-title">Management Quota</div>
                        <div class="card-detail"><strong>Course:</strong> {item['course']}</div>
                        <div class="card-detail" style="color: #60a5fa;"><strong>Annual Fee:</strong> INR {item['fees_per_year']:,}</div>
                    </div>
                    """,
              unsafe_allow_html=True,
          )
      for item in fees.get("comedk_fee_structure", []):
        if "Computer Science Engineering" in item["course"]:
          st.markdown(
              f"""
                    <div class="card">
                        <div class="card-title">COMEDK Quota</div>
                        <div class="card-detail"><strong>Course:</strong> {item['course']}</div>
                        <div class="card-detail" style="color: #60a5fa;"><strong>Total Fee:</strong> INR {item['total_fee']:,}</div>
                    </div>
                    """,
              unsafe_allow_html=True,
          )
    else:
      # General fee summary if specific branch not named
      st.markdown("Here is the general institutional fee overview:")
      for item in fees.get("kcet_fee_structure", []):
        st.markdown(
            f"""
                <div class="card">
                    <div class="card-title">{item['category']}</div>
                    <div class="card-detail"><strong>Total Fee:</strong> INR {item['total_fee']:,}</div>
                </div>
                """,
            unsafe_allow_html=True,
        )

  # 3. Check for Portals / Login Links (Results, Odd Sem, Even Sem)
  if (
      "login" in query_lower
      or "result" in query_lower
      or "sem" in query_lower
      or "portal" in query_lower
  ):
    response_found = True
    portals = campus_data.get("portals", {})
    terms = portals.get("terms", {})

    st.markdown(
        f"""
        <div class="card">
            <div class="card-title">Official Institutional Links Found</div>
            <div class="card-detail">- Examination Results: <a href="{portals.get('results')}" target="_blank">Open Result Portal</a></div>
            <div class="card-detail">- Odd Semester Login: <a href="{terms.get('odd_semester')}" target="_blank">Open Odd Sem Portal</a></div>
            <div class="card-detail">- Even Semester Login: <a href="{terms.get('even_semester')}" target="_blank">Open Even Sem Portal</a></div>
            <div class="card-detail">- General Webfiles: <a href="{portals.get('general_webfiles')}" target="_blank">Open Webfiles Directory</a></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

  if not response_found:
    st.error(
        f"I searched institutional records for '{user_query}', but found no"
        " direct match. Try asking about 'AIML fee', 'CSE fee', 'DBMS exam',"
        " 'results', or 'login'."
    )
else:
  # Default greeting/prompt when chat input is empty
  st.markdown(
      """
    <div class="card">
        <div class="card-title">Welcome to College Saathi AI</div>
        <div class="card-detail">Type your query above to instantly retrieve exam timetables, fee structures for AIML/CSE, or official login portal links.</div>
    </div>
    """,
      unsafe_allow_html=True,
)
      
