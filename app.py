# app.py
import streamlit as st
from api_handler import ChatBackend

st.set_page_config(page_title="Career Advisor AI", page_icon="💼")
st.title("💼 AI Career Advisor")

# Session-based memory management
if "backend" not in st.session_state:
    st.session_state.backend = ChatBackend()
    st.session_state.messages = []

# Conversation history display
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_input := st.chat_input("Ask about interviews, resumes, or career paths..."):
    
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Loading indicator
    with st.spinner("Analyzing your profile..."):
        bot_response = st.session_state.backend.get_response(user_input)
    
    with st.chat_message("assistant"):
        st.markdown(bot_response)
        
    st.session_state.messages.append({"role": "assistant", "content": bot_response})