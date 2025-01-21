from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os
import streamlit as st

load_dotenv()

# Check if running in Streamlit Cloud
if "STREAMLIT_ENV" in os.environ:  # Custom check; Streamlit Cloud doesn't set a specific var
    groq_api_key = st.secrets["GROQ_API_KEY"]
else:
    load_dotenv()  # Load .env for local development
    groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(groq_api_key=groq_api_key, model_name="llama-3.3-70b-versatile")

if __name__ == "__main__":
    response = llm.invoke("What are the two important ingredients in samosa?")
    print(response.content)