from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{question}")
])

# step 1 - format the prompt
prompt_value = prompt.invoke({"question": "What is FastAPI in one sentence?"})

# step 2 - call the llm
ai_message = llm.invoke(prompt_value)
print(type(ai_message))  # AIMessage
print(ai_message)

# step 3 - parse
parser = StrOutputParser()
result = parser.invoke(ai_message)
print(type(result))  # str
print(result)



prompt2 = ChatPromptTemplate.from_messages([
    ("system", "Return a JSON object only. No explanation."),
    ("human", "Give me details about {language}. Fields: name, year_created, creator, use_case.")
])

prompt_value2 = prompt2.invoke({"language": "Python"})
ai_message2 = llm.invoke(prompt_value2)

parser2 = JsonOutputParser()
result2 = parser2.invoke(ai_message2)
print(type(result2))  # dict
print(result2["creator"])