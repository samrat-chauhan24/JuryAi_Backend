from pydantic import BaseModel
from typing import List


class Analysis(BaseModel):
    explanation: str = ""
    conditions: List[str] = []
    risks: List[str] = []


class LegalResponse(BaseModel):
    answer: str
    risk: str
    summary: str

    analysis: Analysis

    references: List[str]