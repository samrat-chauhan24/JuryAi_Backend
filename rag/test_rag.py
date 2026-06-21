from rag.retriever import retrieve
from rag.query_classifier import detect_acts


query = "Can the Indian government restrict freedom of speech?"

country = "india"

print("\n" + "=" * 100)
print(f"QUERY: {query}")
print(f"COUNTRY: {country}")
print(f"DETECTED ACTS: {detect_acts(query)}")
print("=" * 100)

result = retrieve(
    query=query,
    country=country,
    k=6
)

docs = result["documents"]
scores = result["scores"]
best_score = result["best_score"]

print("\n")
print("=" * 100)
print(f"RETRIEVED: {len(docs)} chunks")
print(f"BEST SCORE: {best_score:.4f}")
print("=" * 100)

for i, (doc, score) in enumerate(
    zip(docs, scores),
    start=1
):

    print("\n")
    print("=" * 80)
    print(f"Chunk {i}")
    print("=" * 80)

    print(
        f"Source: "
        f"{doc.metadata.get('source', 'Unknown')}"
    )

    print(
        f"Act: "
        f"{doc.metadata.get('act', 'Unknown')}"
    )

    print(
        f"Country: "
        f"{doc.metadata.get('country', 'Unknown')}"
    )

    print(
        f"Page: "
        f"{doc.metadata.get('page', 'Unknown')}"
    )

    print(
        f"Score: "
        f"{score:.4f}"
    )

    print("\n")

    print(doc.page_content[:1000])

    print("\n")