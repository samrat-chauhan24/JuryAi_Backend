from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from rag.vectorstore import get_vectorstore


ACT_MAPPING = {
    "constitution_india.pdf": "constitution",
    "it_act_2000.pdf": "it_act",
    "dpdp_act_2023.pdf": "dpdp",
    "Companies_Act_2013.pdf": "companies_act",
    "bharat_nyaya_sahita.pdf": "bns",
    "bharat_nyaya_sanhita.pdf": "bns",
    "Bharatiya_Nagarik_Suraksha_2023.pdf": "bnss",
    "Bharatiya_Sakshya_Adhiniyam_2023.pdf": "bsa",
}


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

        loader = PyPDFLoader(
            str(pdf)
        )

        docs = loader.load()

        act_name = ACT_MAPPING.get(
            pdf.name,
            "unknown"
        )

        for doc in docs:

            doc.metadata["source"] = pdf.name

            doc.metadata["country"] = (
                country.lower()
            )

            doc.metadata["act"] = act_name

            # PyPDFLoader already provides page
            doc.metadata["page"] = (
                doc.metadata.get("page", 0)
                + 1
            )

        chunks = splitter.split_documents(
            docs
        )

        all_chunks.extend(chunks)

    db.add_documents(all_chunks)

    print(
        f"\nStored "
        f"{len(all_chunks)} chunks "
        f"for {country}"
    )


if __name__ == "__main__":
    ingest_country("india")