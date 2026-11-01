import json
import os
import streamlit as st

st.title("College Saathi")
st.subheader("PDA College of Engineering, Kalaburagi")

# Define path safely
dir_name = os.path.abspath(os.path.dirname(__file__))
data_folder = os.path.join(dir_name, "data")
exams_path = os.path.join(data_folder, "exams.json")

# Load Exams JSON with safety check
exam_data = {"exams": []}
if os.path.exists(exams_path):
  try:
    with open(exams_path, "r", encoding="utf-8") as f:
      exam_data = json.load(f)
  except Exception:
    exam_data = {"exams": []}

user_query = st.text_input("Ask about exam dates, subjects, or schedule...")

if user_query:
  matched_responses = []
  query_lower = user_query.lower()

  # Search through every exam in the list
  for exam in exam_data.get("exams", []):
    if (
        query_lower in exam["subject"].lower()
        or query_lower in exam["code"].lower()
        or query_lower in exam["semester"].lower()
    ):
      matched_responses.append(
          f"📅 **Exam Found ({exam['semester']}):**\n\n"
          f"- **Subject:** {exam['subject']} ({exam['code']})\n"
          f"- **Date:** {exam['date']}\n"
          f"- **Session:** {exam['session']}"
      )

  if matched_responses:
    # Display all matching results found
    for resp in matched_responses:
      st.markdown(f"**[College Saathi AI]:**\n\n{resp}")
  else:
    st.markdown(
        "**[College Saathi AI]:** No matching record found. Try searching for"
        " 'Data Science', 'Machine Learning', 'DBMS', 'HCI', 'Research',"
        " or 'Environmental'."
    )
    
