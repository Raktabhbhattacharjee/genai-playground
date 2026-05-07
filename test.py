import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load your .env file
load_dotenv()

# Initialize Gemini with the 2026 Free Tier "Learning" model
# 'gemini-2.5-flash-lite' is fast and has the highest daily request limit
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.7
)

# Quick test
try:
    response = llm.invoke("explain gen ai to someone who is a backned guy ?")
    print(f"Model Response:\n{response.content}")
except Exception as e:
    print(f"Error: {e}")
