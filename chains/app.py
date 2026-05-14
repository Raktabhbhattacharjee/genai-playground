# chains/app.py
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
parser = StrOutputParser()

prompt1 = ChatPromptTemplate.from_messages([
    ("system", "You are a Gen AI expert talking to a backend developer."),
    ("human", "Explain Gen AI to a backend developer in simple terms.")
])

prompt2 = ChatPromptTemplate.from_messages([
    ("system", "You are a career advisor for backend developers."),
    ("human", "Based on this explanation of Gen AI:\n\n{text}\n\nShould a backend developer learn basic ML and DL? Give a clear yes/no with 3 reasons.")
])

chain = prompt1 | llm | parser | prompt2 | llm | parser

st.title("Gen AI for Backend Devs")

if st.button("Run"):
    with st.spinner("Thinking..."):
        result = chain.invoke({})
    st.write(result)