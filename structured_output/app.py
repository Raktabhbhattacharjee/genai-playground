import streamlit as st
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

class Person(BaseModel):
    name: str
    age: int
    skills: list[str]

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
structured_llm = llm.with_structured_output(Person)

st.title("Person Info Extractor")

text = st.text_area("Paste any text about a person", placeholder="e.g. Rishi is 21 years old and knows Python, FastAPI and LangChain")

if st.button("Extract"):
    response = structured_llm.invoke(text)
    st.write("**Name:**", response.name)
    st.write("**Age:**", response.age)
    st.write("**Skills:**", response.skills)