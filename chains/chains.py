# chains/chains.py
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
parser = StrOutputParser()

# sequential chain - pipe way
prompt1 = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Explain {topic} in detail.")
])

prompt2 = ChatPromptTemplate.from_messages([
    ("system", "You are a summarizer."),
    ("human", "Summarize this in 3 bullet points:\n\n{text}")
])

chain = prompt1 | llm | parser | prompt2 | llm | parser

result = chain.invoke({"topic": "Gen ai for backned devlopers how to learn it  "})
print(result)