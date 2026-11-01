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
user_query = st.text_input("Ask about exams, circulars, or campus FAQs...")

if user_query:
  matched_answer = None
  for item in knowledge_base.get("faqs", []):
    if any(
        word in user_query.lower() for word in item["question"].lower().split()
    ):
      matched_answer = item["answer"]
      break

  if matched_answer:
    st.markdown(f"**[College Saathi AI]:** {matched_answer}")
  else:
    st.markdown(
        "**[College Saathi AI]:** No direct local record found. Please check"
        " official PDA College notices."
    )
      
