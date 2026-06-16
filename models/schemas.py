from pydantic import BaseModel

class ChatRequest(BaseModel):
    query: str
    jurisdiction: str
    countries: list[str]
    mode: str