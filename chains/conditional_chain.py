from langchain_core.runnables import RunnableBranch, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
parser = StrOutputParser()

# --- Three branches for different feedback types ---

positive_prompt = ChatPromptTemplate.from_template(
    "Write a warm thank you response for this positive feedback:\n{feedback}"
)

negative_prompt = ChatPromptTemplate.from_template(
    "Write a single short empathetic apology and resolution for this negative feedback. "
    "No options, no bullet points, just one response.\n\nFeedback: {feedback}"
)

neutral_prompt = ChatPromptTemplate.from_template(
    "Write a professional acknowledgement for this neutral feedback:\n{feedback}"
)

positive_chain = positive_prompt | model | parser
negative_chain = negative_prompt | model | parser
neutral_chain = neutral_prompt | model | parser

# --- Classifier — decides which branch runs ---

classifier_prompt = ChatPromptTemplate.from_template(
    "Classify this feedback as 'positive', 'negative', or 'neutral'.\n"
    "Reply with one word only.\n\nFeedback: {feedback}"
)

classifier_chain = classifier_prompt | model | parser

# --- Branch router ---

branch = RunnableBranch(
    (lambda x: "positive" in x["sentiment"], positive_chain),
    (lambda x: "negative" in x["sentiment"], negative_chain),
    neutral_chain,  # default fallback
)

# --- Full pipeline ---


def add_sentiment(x: dict) -> dict:
    sentiment = classifier_chain.invoke(x).lower()
    print("Classifier output:", sentiment)  # add this
    return {"feedback": x["feedback"], "sentiment": sentiment}


full_chain = RunnableLambda(add_sentiment) | branch

result = full_chain.invoke({"feedback": "Your product is thrash!"})
print(result)
