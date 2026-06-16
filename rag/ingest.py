from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from rag.vectorstore import get_vectorstore


def ingest_country(country: str):

    db = get_vectorstore(country)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    pdf_folder = Path(
        f"rag/documents/{country.lower()}"
    )

    all_chunks = []

    for pdf in pdf_folder.glob("*.pdf"):

        print(f"Loading {pdf.name}")

        loader = PyPDFLoader(str(pdf))

        docs = loader.load()

        chunks = splitter.split_documents(docs)

        for chunk in chunks:
            chunk.metadata["source"] = pdf.name
            chunk.metadata["country"] = country

        all_chunks.extend(chunks)

    db.add_documents(all_chunks)

    print(
        f"\nStored {len(all_chunks)} chunks for {country}"
    )


if __name__ == "__main__":
    ingest_country("india")