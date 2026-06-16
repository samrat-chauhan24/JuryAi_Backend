def formatter_node(state):

    answer = state["answer"]

    if isinstance(answer, list):

        formatted = []

        for item in answer:

            formatted.append({
                "country": item.get("country", ""),
                "answer": item.get("answer", ""),
                "risk": item.get("risk", ""),
                "summary": item.get("summary", ""),
                "analysis": item.get(
                    "analysis",
                    {}
                ),
                "references": item.get(
                    "references",
                    []
                )
            })

        state["answer"] = formatted

    else:

        state["answer"] = {
            "answer": answer.get(
                "answer",
                ""
            ),

            "risk": answer.get(
                "risk",
                ""
            ),

            "summary": answer.get(
                "summary",
                ""
            ),

            "analysis": answer.get(
                "analysis",
                {}
            ),

            "references": answer.get(
                "references",
                []
            )
        }

    return state