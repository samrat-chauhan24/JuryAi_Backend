# rag/test_rag.py

from rag.retriever import retrieve

query = "What is the Information Technology Act 2000?"

country = "india"

result = retrieve(
    query=query,
    country=country,
    k=6
)

docs = result["documents"]
scores = result["scores"]
best_score = result["best_score"]

print("\n" + "=" * 100)
print(f"QUERY: {query}")
print(f"COUNTRY: {country}")
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
        f"Source: {doc.metadata.get('source', 'Unknown')}"
    )

    print(
        f"Country: {doc.metadata.get('country', 'Unknown')}"
    )

    print(
        f"Score: {score:.4f}"
    )

    print("\n")

    print(doc.page_content[:1000])

    print("\n")