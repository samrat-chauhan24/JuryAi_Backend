from typing import TypedDict


class LegalState(TypedDict):

    query: str

    jurisdiction: str
    countries: list[str]

    mode: str

    prompt: str

    # RAG
    documents: list[str]
    references: list[str]
    citations: list[dict]
    best_retrieval_score: float

    # Final AI response
    answer: dict