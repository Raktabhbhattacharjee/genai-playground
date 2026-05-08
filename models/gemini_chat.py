from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
llm =ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.7,
    max_tokens=100
    
)
result =llm.invoke("hello are you working ")
print(result.content)

# maxtoken no of words 
# temp contoling your model basiclly the tone of your model