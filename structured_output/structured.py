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

response = structured_llm.invoke("Rishi is 21 years old and knows Python, FastAPI and LangChain")

print(response.name)    
print(response.age)
print(response.skills)  