import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from prompt import prompt  # direct import since same folder

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.7,
    max_tokens=3000
)

st.title("Gen AI Roadmap Generator")

ml_level = st.text_input("Your ML/DL level", placeholder="e.g. basic ML, no DL yet")
backend_experience = st.text_input("Backend experience", placeholder="e.g. FastAPI, PostgreSQL, Docker")
tools = st.text_input("Tools you know", placeholder="e.g. LangChain, Groq, Gemini API")
goal = st.text_input("Your goal", placeholder="e.g. Applied AI internship")

if st.button("Generate Roadmap"):
    chain = prompt | llm
    response = chain.invoke({
        "ml_level": ml_level,
        "backend_experience": backend_experience,
        "tools": tools,
        "goal": goal
    })
    st.markdown(response.content)