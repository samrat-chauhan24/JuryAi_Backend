from groq import Groq

from config.settings import GROQ_API_KEY

client = Groq(
    api_key=GROQ_API_KEY
)


def ask_groq(
    prompt: str,
    query: str
) -> str:

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            temperature=0.2,

            messages=[
                {
                    "role": "system",
                    "content": prompt
                },
                {
                    "role": "user",
                    "content": query
                }
            ]
        )

        content = response.choices[0].message.content

        if not content:
            raise Exception(
                "Empty response from Groq"
            )

        # Remove markdown if model adds it
        content = (
            content
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        print("\n===== GROQ RESPONSE =====")
        print(content)
        print("=========================\n")

        return content

    except Exception as e:

        print(
            f"GROQ ERROR: {e}"
        )

        return """
{
  "answer": "Informational",
  "risk": "None",
  "summary": "Unable to generate response.",

  "analysis": {
    "explanation": "An internal error occurred while processing the request.",
    "conditions": [],
    "risks": []
  },

  "references": []
}
"""