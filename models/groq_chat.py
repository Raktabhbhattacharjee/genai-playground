from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv() 

# Initializing the reasoning model
model = ChatGroq(model="llama-3.3-70b-versatile")

# The question you wanted to ask
question = "Explain the difference between open-source and closed-source AI models. Give examples of each."

print("--- Querying Groq (DeepSeek-R1) ---")

# Getting the response
response = model.invoke(question)

# Printing the result
print(response.content)
