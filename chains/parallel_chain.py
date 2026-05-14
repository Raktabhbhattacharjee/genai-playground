from langchain_core.runnables import RunnableParallel, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
parser = StrOutputParser()

# --- Three independent prompts on the same input ---

pros_prompt = ChatPromptTemplate.from_template(
    "List 3 pros of {technology} for backend systems. Be concise."
)

cons_prompt = ChatPromptTemplate.from_template(
    "List 3 cons of {technology} for backend systems. Be concise."
)

usecases_prompt = ChatPromptTemplate.from_template(
    "List 3 real world use cases of {technology} in production. Be concise."
)

# --- Three independent chains ---

pros_chain    = pros_prompt    | model | parser
cons_chain    = cons_prompt    | model | parser
usecase_chain = usecases_prompt | model | parser

# --- Parallel: all three run on the same input simultaneously ---

parallel_chain = RunnableParallel({
    "pros":      pros_chain,
    "cons":      cons_chain,
    "use_cases": usecase_chain,
})

# --- Merge + summarize downstream ---

def merge(outputs: dict) -> dict:
    return {
        "analysis": (
            f"Pros:\n{outputs['pros']}\n\n"
            f"Cons:\n{outputs['cons']}\n\n"
            f"Use Cases:\n{outputs['use_cases']}"
        )
    }

summary_prompt = ChatPromptTemplate.from_template(
    "Based on this analysis:\n{analysis}\n\nGive a 2 line recommendation."
)

summary_chain = summary_prompt | model | parser

# --- Full pipeline ---

full_chain = parallel_chain | RunnableLambda(merge) | summary_chain

result = full_chain.invoke({"technology": "Node js"})
print(result)