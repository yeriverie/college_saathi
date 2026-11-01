import json
import os
import streamlit as st

st.title("College Saathi")
st.subheader("PDA College of Engineering, Kalaburagi")

# Load your notices.json dataset safely
dir_name = os.path.abspath(os.path.dirname(__file__))
data_path = os.path.join(dir_name, "notices.json")

if os.path.exists(data_path):
  with open(data_path, "r", encoding="utf-8") as f:
    knowledge_base = json.load(f)
else:
  knowledge_base = {"faqs": []}

# Chat input box
user_query = st.text_input("Ask about exam dates, subjects, or schedule...")

if user_query:
  matched_response = None
  query_lower = user_query.lower()

  for exam in exam_data.get("exams", []):
    # Check if any keyword from the query matches the subject or code
    if (
        query_lower in exam["subject"].lower()
        or query_lower in exam["code"].lower()
        or query_lower in exam["semester"].lower()
    ):
      matched_response = (
          f"📅 **Exam Found ({exam['semester']}):**\n\n"
          f"- **Subject:** {exam['subject']} ({exam['code']})\n"
          f"- **Date:** {exam['date']}\n"
          f"- **Session:** {exam['session']}"
      )
      break

  if matched_response:
    st.markdown(f"**[College Saathi AI]:**\n\n{matched_response}")
  else:
    st.markdown(
        "**[College Saathi AI]:** No matching record found. Try typing part of"
        " the subject name like 'Data Science', 'Machine Learning', or"
        " 'DBMS'."
    )
    
