# graph/nodes/llm.py

import json

from services.groq_service import ask_groq


def llm_node(state):

    print("\n=== LLM NODE ENTERED ===")

    print(
        f"Documents Received: "
        f"{len(state.get('documents', []))}"
    )

    print(
        f"References Received: "
        f"{state.get('references', [])}"
    )

    context = "\n\n".join(
        state.get("documents", [])
    )
    print(f"Context Length: {len(context)}")

    full_prompt = state["prompt"]

    if context:

        full_prompt += f"""

Retrieved Legal Context:

{context}

Instructions:
- Prioritize the retrieved legal context when answering.
- If the retrieved context is insufficient, answer using general legal knowledge.
- Do not invent legal citations.
- Mention uncertainty when the retrieved context does not directly answer the question.
"""

    response = ask_groq(
        prompt=full_prompt,
        query=state["query"]
    )

    state["answer"] = json.loads(response)

    return state
