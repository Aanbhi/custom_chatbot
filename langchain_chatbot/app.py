# app.py
import os
from flask import Flask, request, jsonify
from langchain.document_loaders import WebBaseLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.schema import Document
from dotenv import load_dotenv

# Load env vars
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

# Load and process data
URL = "https://brainlox.com/courses/category/technical"
loader = WebBaseLoader(URL)
documents = loader.load()
documents = [Document(page_content=doc.page_content, metadata={"source": URL}) for doc in documents[:10]]

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
texts = [doc.page_content for doc in documents]
db = FAISS.from_texts(texts, embeddings)
db.save_local("faiss_index")
retriever = db.as_retriever()

# Chat Chain
llm = OpenAI(api_key=openai_api_key)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever, memory=memory)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    if not user_message:
        return jsonify({"error": "No message received"}), 400
    try:
        response = chain.run({"question": user_message})
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
