import streamlit as st

st.set_page_config(page_title="College Saathi - PDACE", page_icon="🎓")

st.title("🎓 College Saathi")
st.subheader("PDA College of Engineering, Kalaburagi")
st.caption("Your 24/7 AI Campus Assistant")

# Sample PDACE knowledge base FAQs
KNOWLEDGE_BASE = {
    "cie": "The Continuous Internal Evaluation (CIE) exams for PDACE are conducted according to the academic calendar. Please check your department notice board for exact time slots.",
    "cse": "The Computer Science and Engineering (CSE) department syllabus covers Data Structures, DBMS, AI/ML, OS, and Computer Networks under autonomous regulation.",
    "fee": "Tuition fees can be paid online via the official college portal or through the administrative office counter.",
    "placement": "The Smart Campus Placement Cell organizes training and campus recruitment drives for final and pre-final year students.",
}

# Quick action buttons for PDACE students
col1, col2 = st.columns(2)
with col1:
    if st.button("📅 CIE & Exam Schedule"):
        st.session_state.prompt_input = "Tell me about CIE exam schedule"
with col2:
    if st.button("📚 CSE Syllabus & Notes"):
        st.session_state.prompt_input = "What is the CSE syllabus?"

# Initialize chat session
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display message history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Handle user input
user_query = st.chat_input("Ask about exams, circulars, or campus FAQs...")

# Support button clicks
if "prompt_input" in st.session_state and st.session_state.prompt_input:
    user_query = st.session_state.prompt_input
    st.session_state.prompt_input = ""

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    query_lower = user_query.lower()
    bot_reply = "I'm College Saathi! I can help with PDACE CIE schedules, CSE syllabus, fees, and placement details. Could you specify your question?"
    
    for key, info in KNOWLEDGE_BASE.items():
        if key in query_lower:
            bot_reply = info
            break

    with st.chat_message("assistant"):
        st.markdown(f"**[College Saathi AI]:** {bot_reply}")
    st.session_state.messages.append({"role": "assistant", "content": f"**[College Saathi AI]:** {bot_reply}"})
    
