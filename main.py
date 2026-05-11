from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()

from outputs.service import parse_ticket  # import your service

app = FastAPI()


class InputRequest(BaseModel):
    text: str


@app.post("/parse")
def parse(req: InputRequest):
    try:
        ticket = parse_ticket(req.text)
        return {
            "success": True,
            "data": ticket.model_dump()
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))