from rag.vectorstore import get_vectorstore


def retrieve(
    query: str,
    country: str,
    k: int = 6
):

    db = get_vectorstore(country)

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