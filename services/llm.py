import os
from openai import OpenAI
from dotenv import load_dotenv
from schemas.models import Message

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    api_key=API_KEY,
    base_url="https://openrouter.ai/api/v1"
)



SYSTEM_PROMPT = """
You are a helpful customer support assistant.

Use the previous conversation provided in the input to answer the user's current question.

If the user provided personal information earlier in the conversation,
such as their name, use that information when relevant.

Do not say that you cannot access information if that information
is already present in the conversation history.
"""


def stream_support_response(
    message: str,
    history: list[Message]
):
    try:
        conversation = []

        for item in history:
            conversation.append({
                "role": item.role,
                "content": item.content,
            })

        conversation.append({
            "role": "user",
            "content": message,
        })

        stream = client.responses.create(
            model="gpt-4o-mini",
            instructions=SYSTEM_PROMPT,
            input=conversation,
            stream=True,
        )

        for event in stream:
            if event.type == "response.output_text.delta":
                yield event.delta

    except Exception as e:
        print("LLM ERROR:", e)
        yield "Sorry, the AI service is temporarily unavailable."

   