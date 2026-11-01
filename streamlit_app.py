import json
import os
import streamlit as st

st.title("College Saathi")
st.subheader("PDA College of Engineering, Kalaburagi")

# Safely locate data directory
dir_name = os.path.abspath(os.path.dirname(__file__))
data_folder = os.path.join(dir_name, "data")
exams_path = os.path.join(data_folder, "exams.json")

# Load JSON Data safely
exam_data = {"exams": []}
if os.path.exists(exams_path):
  try:
    with open(exams_path, "r", encoding="utf-8") as f:
      exam_data = json.load(f)
  except Exception:
    exam_data = {"exams": []}

user_query = st.text_input(
    "Ask about exam dates. Just for now demo one." 
    
)

if user_query:
  matched_responses = []
  query_lower = user_query.strip().lower()

  # Smart Acronym & Short-form mapping for PDA College subjects
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

  # Expand search terms if user types a short form
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
      resp = (
          f"📅 **Exam Found ({exam['semester']}):**\n\n"
          f"- **Subject:** {exam['subject']} ({exam['code']})\n"
          f"- **Date:** {exam['date']}\n"
          f"- **Session:** {exam['session']}"
      )
      if resp not in matched_responses:
        matched_responses.append(resp)

  if matched_responses:
    st.markdown("**[College Saathi AI]:**")
    for resp in matched_responses:
      st.markdown(resp)
      st.markdown("---")
  else:
    st.markdown(
        "**[College Saathi AI]:** No matching record found for"
        f" '{user_query}'. Try searching for 'DBMS', 'Machine Learning',"
        " 'Data Science', or 'HCI'."
    )
    
