from langchain.agents import create_agent
from outputs.output import Ticket

agent = create_agent(
    model="google_genai:gemini-2.5-flash-lite",
    tools=[],
    response_format=Ticket
)

def parse_ticket(text: str) -> Ticket:
    res = agent.invoke({
        "messages": [
            {"role": "user", "content": text}
        ]
    })
    return res["structured_response"]