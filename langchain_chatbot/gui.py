# gui.py
import streamlit as st
import requests

st.title("🧠 LangChain Brainlox Chatbot")

backend_url = st.text_input("Backend URL (Flask)", "http://127.0.0.1:5000/chat")

if "history" not in st.session_state:
    st.session_state.history = []

message = st.text_input("Ask a question about Brainlox courses:")

if st.button("Send") and message:
    try:
        res = requests.post(backend_url, json={"message": message})
        res_data = res.json()
        response = res_data.get("response")
        if response:
            st.session_state.history.append(("You", message))
            st.session_state.history.append(("Bot", response))
        else:
            st.error(res_data.get("error", "Unknown error"))
    except Exception as e:
        st.error(f"Connection Error: {e}")

for sender, msg in st.session_state.history:
    st.markdown(f"**{sender}:** {msg}")
