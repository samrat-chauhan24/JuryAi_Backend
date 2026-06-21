from groq import Groq

from config.settings import GROQ_API_KEY


client = Groq(
    api_key=GROQ_API_KEY
)


def stream_groq(
    prompt: str,
    query: str
):

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": query
            }
        ],
        temperature=0,
        stream=True
    )

    for chunk in completion:

        token = chunk.choices[0].delta.content

        print("CONTENT:", token)

        if token:
            yield token