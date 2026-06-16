from fastapi import APIRouter

from models.schemas import ChatRequest
from graph.graph import graph

router = APIRouter()


@router.post("/chat")
async def chat(request: ChatRequest):

    result = graph.invoke(
        {
            "query": request.query,

            "jurisdiction": request.jurisdiction,

            "countries": request.countries,

            "mode": request.mode,

            "prompt": "",

            "answer": {}
        }
    )

    return result["answer"]