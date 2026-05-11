from pydantic import BaseModel, Field
from typing import Literal

class Ticket(BaseModel):
    name: str = Field(description="Customer name")
    email: str = Field(description="Customer email")
    issue: str = Field(description="What the problem is")
    priority: Literal["low", "medium", "high"]