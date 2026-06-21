from rag.retriever import retrieve


def rag_node(state):

    print("\n=== RAG NODE ENTERED ===")
    print(f"Jurisdiction: {state['jurisdiction']}")
    print(f"Countries: {state['countries']}")

    # Defaults
    state["documents"] = []
    state["references"] = []
    state["citations"] = []
    state["best_retrieval_score"] = 999.0

    # RAG only for specific-country mode
    if state["jurisdiction"] != "specific country":
        return state

    if not state["countries"]:
        return state

    country = state["countries"][0].lower()

    try:

        result = retrieve(
            query=state["query"],
            country=country,
            k=3
        )

        docs = result["documents"]

        # Context for LLM
        state["documents"] = [
            doc.page_content
            for doc in docs
        ]

        # Unique source files
        state["references"] = list(
            {
                doc.metadata.get("source")
                for doc in docs
                if doc.metadata.get("source")
            }
        )

        # Unique citations
        seen = set()
        citations = []

        for doc in docs:

            source = doc.metadata.get(
                "source",
                "unknown"
            )

            page = doc.metadata.get(
                "page",
                None
            )

            key = (source, page)

            if key not in seen:

                seen.add(key)

                citations.append(
                    {
                        "source": source,
                        "page": page
                    }
                )

        state["citations"] = citations

        state["best_retrieval_score"] = (
            result["best_score"]
        )

        print(
            f"Retrieved Chunks: "
            f"{len(state['documents'])}"
        )

        print(
            f"Sources: "
            f"{state['references']}"
        )

        print(
            f"Citations: "
            f"{len(state['citations'])}"
        )

        print(
            f"Best Score: "
            f"{state['best_retrieval_score']}"
        )

    except Exception as e:

        print(f"RAG Error: {e}")

        state["documents"] = []
        state["references"] = []
        state["citations"] = []
        state["best_retrieval_score"] = 999.0

    return state