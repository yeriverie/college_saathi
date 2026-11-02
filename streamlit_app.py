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
    a {
        color: #60a5fa;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
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
        "management_quota_fees_per_year": [
            {
                "course": (
                    "Artificial Intelligence and Machine Learning (AIML)"
                ),
                "fees_per_year": 250000,
            },
            {
                "course": "Computer Science Engineering (CSE)",
                "fees_per_year": 250000,
            },
        ],
        "comedk_fee_structure": [
            {
                "course": (
                    "Artificial Intelligence and Machine Learning (AIML)"
                ),
                "tuition_fee": 186000,
                "other_fee": 20000,
                "university_fee_payable_at_college": 10610,
                "total_fee": 216610,
            },
            {
                "course": "Computer Science Engineering (CSE)",
                "tuition_fee": 186000,
                "other_fee": 20000,
                "university_fee_payable_at_college": 10610,
                "total_fee": 216610,
            },
        ],
    },
    "syllabus": {
        "aiml": [
            "Data Science & Its Applications (22AI51)",
            "Database Management System (22AI52)",
            "Principles of Machine Learning (22AI53)",
            "Human Computer Interface (22AI55A)",
            "Research Methodology and IPR (22RM157)",
            "Environmental Studies (22ES58)",
        ],
        "cse": [
            "Data Structures & Algorithms",
            "Design & Analysis of Algorithms",
            "Operating Systems",
            "Computer Networks",
            "Database Management Systems",
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
    "Ask anything about exams, fees, syllabus, or portals...",
    placeholder=(
        "Try 'AIML fee', 'CSE syllabus', 'result link', or 'odd sem login'..."
    ),
)

if user_query:
  query_lower = user_query.strip().lower()
  response_found = False

  st.markdown("**[College Saathi AI]:**")

  # INTENT 1: FEE STRUCTURE (AIML or CSE)
  if "fee" in query_lower:
    response_found = True
    fees = campus_data.get("fee_structure", {})

    if "aiml" in query_lower or "artificial intelligence" in query_lower:
      st.markdown(
          "Fee Structure for Artificial Intelligence and Machine Learning"
          " (AIML):"
      )
      for item in fees.get("management_quota_fees_per_year", []):
        if "Artificial Intelligence" in item["course"]:
          st.markdown(
              f"""
                <div class="card">
                    <div class="card-title">Management Quota</div>
                    <div class="card-detail"><strong>Annual Fee:</strong> INR {item['fees_per_year']:,}</div>
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
                    <div class="card-detail"><strong>Tuition Fee:</strong> INR {item['tuition_fee']:,}</div>
                    <div class="card-detail"><strong>Other Fee:</strong> INR {item['other_fee']:,}</div>
                    <div class="card-detail"><strong>University Fee:</strong> INR {item['university_fee_payable_at_college']:,}</div>
                    <div class="card-detail" style="color: #60a5fa; margin-top: 6px;"><strong>Total Fee:</strong> INR {item['total_fee']:,}</div>
                </div>
                """,
              unsafe_allow_html=True,
          )

    elif "cse" in query_lower or "computer science" in query_lower:
      st.markdown("Fee Structure for Computer Science Engineering (CSE):")
      for item in fees.get("management_quota_fees_per_year", []):
        if "Computer Science Engineering" in item["course"]:
          st.markdown(
              f"""
                <div class="card">
                    <div class="card-title">Management Quota</div>
                    <div class="card-detail"><strong>Annual Fee:</strong> INR {item['fees_per_year']:,}</div>
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
                    <div class="card-detail"><strong>Tuition Fee:</strong> INR {item['tuition_fee']:,}</div>
                    <div class="card-detail"><strong>Other Fee:</strong> INR {item['other_fee']:,}</div>
                    <div class="card-detail"><strong>University Fee:</strong> INR {item['university_fee_payable_at_college']:,}</div>
                    <div class="card-detail" style="color: #60a5fa; margin-top: 6px;"><strong>Total Fee:</strong> INR {item['total_fee']:,}</div>
                </div>
                """,
              unsafe_allow_html=True,
          )
    else:
      st.markdown("General Institutional Fee Overview:")
      st.markdown(
          """
            <div class="card">
                <div class="card-title">KCET Aided / Un-Aided</div>
                <div class="card-detail">Please specify your branch (e.g., 'AIML fee' or 'CSE fee') to view specific quota breakdowns.</div>
            </div>
            """,
          unsafe_allow_html=True,
      )

  # INTENT 2: SYLLABUS (AIML or CSE)
  elif "syllabus" in query_lower or "subject" in query_lower:
    response_found = True
    syllabus = campus_data.get("syllabus", {})

    if "aiml" in query_lower or "artificial intelligence" in query_lower:
      subs = "\n".join([f"- {sub}" for sub in syllabus.get("aiml", [])])
      st.markdown(
          f"""
            <div class="card">
                <div class="card-title">AIML Curriculum & Subjects (V Semester)</div>
                <div class="card-detail">{subs.replace(chr(10), '<br>')}</div>
            </div>
            """,
          unsafe_allow_html=True,
      )
    elif "cse" in query_lower or "computer science" in query_lower:
      subs = "\n".join([f"- {sub}" for sub in syllabus.get("cse", [])])
      st.markdown(
          f"""
            <div class="card">
                <div class="card-title">CSE Curriculum & Subjects</div>
                <div class="card-detail">{subs.replace(chr(10), '<br>')}</div>
            </div>
            """,
          unsafe_allow_html=True,
      )
    else:
      st.markdown(
          """
            <div class="card">
                <div class="card-title">Curriculum Directory</div>
                <div class="card-detail">Please specify branch like 'AIML syllabus' or 'CSE syllabus'.</div>
            </div>
            """,
          unsafe_allow_html=True,
      )

  # INTENT 3: PORTALS, RESULTS & LOGIN (Contineo Links)
  elif (
      "login" in query_lower
      or "result" in query_lower
      or "contineo" in query_lower
      or "portal" in query_lower
      or "sem" in query_lower
  ):
    response_found = True
    portals = campus_data.get("portals", {})
    terms = portals.get("terms", {})

    st.markdown(
        f"""
        <div class="card">
            <div class="card-title">Official Contineo & Student Portals</div>
            <div class="card-detail">- <strong>Examination Results:</strong> <a href="{portals.get('results')}" target="_blank">Open Result Portal</a></div>
            <div class="card-detail">- <strong>Odd Semester Login:</strong> <a href="{terms.get('odd_semester')}" target="_blank">Open Odd Semester Portal</a></div>
            <div class="card-detail">- <strong>Even Semester Login:</strong> <a href="{terms.get('even_semester')}" target="_blank">Open Even Semester Portal</a></div>
            <div class="card-detail">- <strong>Summer Term Login:</strong> <a href="{terms.get('summer_term')}" target="_blank">Open Summer Term Portal</a></div>
            <div class="card-detail">- <strong>General Webfiles:</strong> <a href="{portals.get('general_webfiles')}" target="_blank">Open Webfiles Directory</a></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

  # INTENT 4: EXAMS & SCHEDULES
  elif "exam" in query_lower or "date" in query_lower or "schedule" in query_lower:
    response_found = True
    for exam in campus_data.get("exams", []):
      st.markdown(
          f"""
            <div class="card">
                <div class="card-title">{exam['subject']} ({exam['code']})</div>
                <div class="card-detail"><strong>Date:</strong> {exam['date']}</div>
                <div class="card-detail"><strong>Session:</strong> {exam['session']}</div>
            </div>
            """,
          unsafe_allow_html=True,
      )

  if not response_found:
    st.error(
        f"No direct match for '{user_query}'. Try searching for 'AIML fee',"
        " 'CSE syllabus', 'result link', or 'odd sem login'."
    )
else:
  st.markdown(
      """
    <div class="card">
        <div class="card-title">Welcome to College Saathi AI</div>
        <div class="card-detail">Ask about <strong>AIML/CSE fee structures</strong>, <strong>syllabus</strong>, <strong>exam schedules</strong>, or direct <strong>Contineo login links</strong>.</div>
    </div>
    """,
      unsafe_allow_html=True,
  )
      
