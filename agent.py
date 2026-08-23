import os
from litellm import completion
from dotenv import load_dotenv
load_dotenv()


def process_task(task: str, worker_id: str) -> str | None:
    task_lower = task.lower()

    response = completion(
        model="openai/aisingapore/Gemma-SEA-LION-v4-27B-IT",

        api_key=os.getenv("SEALION_API_KEY"),

        api_base="https://api.sea-lion.ai/v1",

        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            },
            {
                "role": "user",
                "content": task
            }
        ]
    )

    return response.choices[0].message.content # type: ignore
