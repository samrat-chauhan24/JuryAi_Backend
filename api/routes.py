from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from models.schemas import ChatRequest

from graph.graph import graph

from graph.nodes.validator import (
    validator_node
)

from graph.nodes.router import (
    router_node
)

from graph.nodes.rag import (
    rag_node
)

from services.groq_stream_service import (
    stream_groq
)

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

            "documents": [],

            "references": [],

            "best_retrieval_score": 999.0,

            "answer": {}
        }
    )

    return result["answer"]


@router.post("/chat/stream")
async def chat_stream(
    request: ChatRequest
):

    state = {
        "query": request.query,

        "jurisdiction": request.jurisdiction,

        "countries": request.countries,

        "mode": request.mode,

        "prompt": "",

        "documents": [],

        "references": [],

        "best_retrieval_score": 999.0,

        "answer": {}
    }

    state = validator_node(state)

    state = router_node(state)

    state = rag_node(state)

    def generate():
        print("=== STREAM STARTED ===")
        for token in stream_groq(
            prompt=state["prompt"],
            query=state["query"]
        ):
            yield token
        print("\n=== STREAM FINISHED ===")
    return StreamingResponse(
        generate(),
        media_type="text/plain"
    )