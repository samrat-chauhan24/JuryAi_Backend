from rag.vectorstore import get_vectorstore
from rag.query_classifier import detect_acts


def retrieve(
    query: str,
    country: str,
    k: int = 6
):

    db = get_vectorstore(country)

    detected_acts = detect_acts(query)

    print(
        f"Detected Acts: "
        f"{detected_acts}"
    )

    try:

        if detected_acts:

            results = db.similarity_search_with_score(
                query,
                k=k,
                filter={
                    "act": {
                        "$in": detected_acts
                    }
                }
            )

        else:

            results = db.similarity_search_with_score(
                query,
                k=k
            )

    except Exception:

        # Fallback if filter fails
        results = db.similarity_search_with_score(
            query,
            k=k
        )

    documents = []
    scores = []

    for doc, score in results:

        documents.append(doc)

        scores.append(score)

    best_score = (
        min(scores)
        if scores
        else 999.0
    )

    return {
        "documents": documents,
        "scores": scores,
        "best_score": best_score
    }