import json
import os
import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="College Saathi AI",
    layout="centered",
    initial_sidebar_state="expanded",
)

# --- Custom Styling (Dark Theme & Clean Cards) ---
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
        <span class="badge">Hackathon Prototype Demo | Institutional Portal</span>
    </div>
""",
    unsafe_allow_html=True,
)

# --- Load Data Safely from JSON ---
dir_name = os.path.abspath(os.path.dirname(__file__))
data_folder = os.path.join(dir_name, "data")
json_path = os.path.join(data_folder, "campus_data.json")

# Fallback internal dictionary if JSON file is missing locally
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
                "sl_no": 1,
                "course": "All Courses",
                "tuition_fee": 85346,
                "other_fee": 20000,
                "fee_paid_in_comedk": 15000,
                "university_fee_payable_at_college": 10610,
                "total_fee": 130956,
            },
            {
                "category": "KCET (Aided Course)",
                "sl_no": 1,
                "course": "All Courses",
                "tuition_fee": 22256,
                "other_fee": 20000,
                "fee_paid_in_comedk": 15000,
                "university_fee_payable_at_college": 10610,
                "total_fee": 67866,
            },
        ],
        "management_quota_fees_per_year": [
            {
                "sl_no": 1,
                "course": "Civil Engineering",
                "fees_per_year": 140000,
            },
            {
                "sl_no": 2,
                "course": "Mechanical Engineering",
                "fees_per_year": 140000,
            },
            {
                "sl_no": 3,
                "course": "Electrical & Electronics Engineering",
                "fees_per_year": 170000,
            },
            {
                "sl_no": 4,
                "course": "Electronics & Communication Engineering",
                "fees_per_year": 170000,
            },
            {
                "sl_no": 5,
                "course": "Industrial and Production Engineering",
                "fees_per_year": 140000,
            },
            {
                "sl_no": 6,
                "course": "Electronics & Instrumentation Engineering",
                "fees_per_year": 140000,
            },
            {
                "sl_no": 7,
                "course": "Computer Science Engineering",
                "fees_per_year": 250000,
            },
            {
                "sl_no": 8,
                "course": "Computer Science and Design",
                "fees_per_year": 200000,
            },
            {
                "sl_no": 9,
                "course": "Cement and Ceramic Technology",
                "fees_per_year": 140000,
            },
            {
                "sl_no": 10,
                "course": "Information Science Engineering",
                "fees_per_year": 200000,
            },
            {
                "sl_no": 11,
                "course": (
                    "Artificial Intelligence and Machine Learning"
                ),
                "fees_per_year": 250000,
            },
            {
                "sl_no": 12,
                "course": "Artificial Intelligence (AI) and Data Science",
                "fees_per_year": 250000,
            },
        ],
        "comedk_fee_structure": [
            {
                "sl_no": 1,
                "course": "Civil Engineering",
                "tuition_fee": 80000,
                "other_fee": 20000,
                "fee_paid_in_comedk": 100000,
                "university_fee_payable_at_college": 10610,
                "total_fee": 110610,
            },
            {
                "sl_no": 2,
                "course": "Mechanical Engineering",
                "tuition_fee": 80000,
                "other_fee": 20000,
                "fee_paid_in_comedk": 100000,
                "university_fee_payable_at_college": 10610,
                "total_fee": 110610,
            },
            {
                "sl_no": 3,
                "course": "Electrical & Electronics Engineering",
                "tuition_fee": 186000,
                "other_fee": 20000,
                "fee_paid_in_comedk": 206000,
                "university_fee_payable_at_college": 10610,
                "total_fee": 216610,
            },
            {
                "sl_no": 4,
                "course": "Electronics & Communication Engineering",
                "tuition_fee": 186000,
                "other_fee": 20000,
                "fee_paid_in_comedk": 206000,
                "university_fee_payable_at_college": 10610,
                "total_fee": 216610,
            },
            {
                "sl_no": 5,
                "course": "Industrial and Production Engineering",
                "tuition_fee": 80000,
                "other_fee": 20000,
                "fee_paid_in_comedk": 100000,
                "university_fee_payable_at_college": 10610,
                "total_fee": 110610,
            },
            {
                "sl_no": 6,
                "course": "Electronics & Instrumentation Engineering",
                "tuition_fee": 80000,
                "other_fee": 20000,
                "fee_paid_in_comedk": 100000,
                "university_fee_payable_at_college": 10610,
                "total_fee": 110610,
            },
            {
                "sl_no": 7,
                "course": "Computer Science Engineering",
                "tuition_fee": 186000,
                "other_fee": 20000,
                "fee_paid_in_comedk": 206000,
                "university_fee_payable_at_college": 10610,
                "total_fee": 216610,
            },
            {
                "sl_no": 8,
                "course": "Computer Science and Design",
                "tuition_fee": 186000,
                "other_fee": 20000,
                "fee_paid_in_comedk": 206000,
                "university_fee_payable_at_college": 10610,
                "total_fee": 216610,
            },
            {
                "sl_no": 9,
                "course": "Cement and Ceramic Technology",
                "tuition_fee": 80000,
                "other_fee": 20000,
                "fee_paid_in_comedk": 100000,
                "university_fee_payable_at_college": 10610,
                "total_fee": 110610,
            },
            {
                "sl_no": 10,
                "course": "Information Science Engineering",
                "tuition_fee": 186000,
                "other_fee": 20000,
                "fee_paid_in_comedk": 206000,
                "university_fee_payable_at_college": 10610,
                "total_fee": 216610,
            },
            {
                "sl_no": 11,
                "course": (
                    "Artificial Intelligence and Machine Learning"
                ),
                "tuition_fee": 186000,
                "other_fee": 20000,
                "fee_paid_in_comedk": 206000,
                "university_fee_payable_at_college": 10610,
                "total_fee": 216610,
            },
        ],
    },
}

# Try reading from JSON file if it exists, otherwise use default
campus_data = default_data
if os.path.exists(json_path):
  try:
    with open(json_path, "r", encoding="utf-8") as f:
      campus_data = json.load(f)
  except Exception:
    campus_data = default_data

# --- Sidebar Navigation Control Panel ---
st.sidebar.markdown("### Control Panel")
app_mode = st.sidebar.selectbox(
    "Select Navigation View",
    ["Exam Schedule Search", "Fee Structure Details", "Official Portals"],
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    "**Quick Search Keywords:**\n- `DBMS` / `ML` / `Data Science` / `HCI` /"
    " `RM`"
)

# --- MODE 1: Exam Schedule Search ---
if app_mode == "Exam Schedule Search":
  st.markdown("### Smart Exam Schedule Search")
  user_query = st.text_input(
      "Search by subject name, code, or short form",
      placeholder="Type 'DBMS', 'ML', 'Data Science', '22AI51', or 'HCI'...",
  )

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
        card_html = f"""
            <div class="card">
                <div class="card-title">Exam Found ({exam['semester']})</div>
                <div class="card-detail"><strong>Subject:</strong> {exam['subject']} ({exam['code']})</div>
                <div class="card-detail"><strong>Date:</strong> {exam['date']}</div>
                <div class="card-detail"><strong>Session:</strong> {exam['session']}</div>
            </div>
            """
        if card_html not in matched_responses:
          matched_responses.append(card_html)

    st.markdown("**[College Saathi AI]:**")
    if matched_responses:
      for resp in matched_responses:
        st.markdown(resp, unsafe_allow_html=True)
    else:
      st.error(
          f"No matching record found for '{user_query}'. Try searching for"
          " 'DBMS', 'ML', 'Data Science', or 'HCI'."
      )
  else:
    # Display full list by default when input is empty
    st.markdown("### V Semester AI & ML - Examination Schedule")
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

# --- MODE 2: Fee Structure Details ---
elif app_mode == "Fee Structure Details":
  st.markdown("### Institutional Fee Structure Directory")
  fee_tab = st.radio(
      "Select Quota Category",
      ["KCET Quota", "COMEDK Quota", "Management Quota"],
      horizontal=True,
  )

  fees = campus_data.get("fee_structure", {})

  if fee_tab == "KCET Quota":
    st.markdown("#### KCET Fee Breakdown")
    for item in fees.get("kcet_fee_structure", []):
      st.markdown(
          f"""
            <div class="card">
                <div class="card-title">{item['category']}</div>
                <div class="card-detail"><strong>Tuition Fee:</strong> INR {item['tuition_fee']:,}</div>
                <div class="card-detail"><strong>Other Fee:</strong> INR {item['other_fee']:,}</div>
                <div class="card-detail"><strong>University Fee (Payable at College):</strong> INR {item['university_fee_payable_at_college']:,}</div>
                <div class="card-detail" style="color: #60a5fa; margin-top: 8px;"><strong>Total Fee:</strong> INR {item['total_fee']:,}</div>
            </div>
            """,
          unsafe_allow_html=True,
      )

  elif fee_tab == "COMEDK Quota":
    st.markdown("#### COMEDK Fee Breakdown by Department")
    for item in fees.get("comedk_fee_structure", []):
      st.markdown(
          f"""
            <div class="card">
                <div class="card-title">{item['course']}</div>
                <div class="card-detail"><strong>Tuition Fee:</strong> INR {item['tuition_fee']:,}</div>
                <div class="card-detail"><strong>Other Fee:</strong> INR {item['other_fee']:,}</div>
                <div class="card-detail"><strong>University Fee:</strong> INR {item['university_fee_payable_at_college']:,}</div>
                <div class="card-detail" style="color: #60a5fa; margin-top: 8px;"><strong>Total Fee:</strong> INR {item['total_fee']:,}</div>
            </div>
            """,
          unsafe_allow_html=True,
      )

  elif fee_tab == "Management Quota":
    st.markdown("#### Management Quota Annual Fee Structure")
    for item in fees.get("management_quota_fees_per_year", []):
      st.markdown(
          f"""
            <div class="card">
                <div class="card-title">{item['course']}</div>
                <div class="card-detail" style="color: #60a5fa;"><strong>Fees Per Year:</strong> INR {item['fees_per_year']:,}</div>
            </div>
            """,
          unsafe_allow_html=True,
      )

# --- MODE 3: Official Portals & Links ---
elif app_mode == "Official Portals":
  st.markdown("### Official Institutional Portals")
  portals = campus_data.get("portals", {})
  terms = portals.get("terms", {})

  st.markdown(
      f"""
    <div class="card">
        <div class="card-title">Student & Result Portals</div>
        <div class="card-detail">- <a href="{portals.get('results')}" target="_blank">Examination Results Portal</a></div>
        <div class="card-detail">- <a href="{portals.get('general_webfiles')}" target="_blank">General Webfiles Directory</a></div>
    </div>
    <div class="card">
        <div class="card-title">Semester Portals</div>
        <div class="card-detail">- <a href="{terms.get('odd_semester')}" target="_blank">Odd Semester Parent Portal</a></div>
        <div class="card-detail">- <a href="{terms.get('even_semester')}" target="_blank">Even Semester Parent Portal</a></div>
        <div class="card-detail">- <a href="{terms.get('summer_term')}" target="_blank">Summer Term Portal</a></div>
    </div>
    """,
      unsafe_allow_html=True,
)
        
