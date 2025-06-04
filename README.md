# 🤖 LangChain  Chatbot

A custom chatbot built using LangChain to extract and converse over data scraped from Brainlox courses.

## 🔧 Features

- Scrapes data from: [Brainlox Technical Courses](https://brainlox.com/courses/category/technical)
- Embeds using Sentence Transformers + FAISS
- Flask REST API for LLM-powered Q&A
- Streamlit UI for interactive chat

## 🚀 How to Run

### 1. Install requirements

pip install -r requirements.txt


File =

langchain_chatbot/

├── app.py                     # Flask API

├── gui.py                     # Streamlit UI

├── requirements.txt           # All dependencies

├── faiss_index/               # Vector store (auto-generated)

├── .env                       # For API keys (add to .gitignore)

├── README.md                  # Project overview & instructions

## ✅ Final Checklist Before Submission

- [x] Flask API handles `/chat` POST requests
      
- [x] LangChain document loader used from Brainlox
      
- [x] FAISS vector store created and used
      
- [x] Streamlit UI for user interaction
      
- [x] `.env` for keys (excluded in `.gitignore`)
      
- [x] Public GitHub repo with `README.md`
