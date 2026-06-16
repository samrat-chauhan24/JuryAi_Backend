from rag.retriever import retrieve


def rag_node(state):
    print("\n=== RAG NODE ENTERED ===")
    print(f"Jurisdiction: {state['jurisdiction']}")
    print(f"Countries: {state['countries']}")
    # Defaults
    state["documents"] = []
    state["references"] = []
    state["best_retrieval_score"] = 999.0

    # RAG only for country mode
    if state["jurisdiction"] != "specific country":
        return state

    if not state["countries"]:
        return state

    country = state["countries"][0].lower()

    try:

        result = retrieve(
            query=state["query"],
            country=country,
            k=6
        )

        docs = result["documents"]

        state["documents"] = [
            doc.page_content
            for doc in docs
        ]

        state["references"] = list(
            {
                doc.metadata.get("source")
                for doc in docs
                if doc.metadata.get("source")
            }
        )

        state["best_retrieval_score"] = (
            result["best_score"]
        )
        print(f"Retrieved Chunks: {len(state['documents'])}")
        print(f"Sources: {state['references']}")
        print(f"Best Score: {state['best_retrieval_score']}")
    except Exception as e:

        print(f"RAG Error: {e}")

        state["documents"] = []
        state["references"] = []
        state["best_retrieval_score"] = 999.0

    return state
