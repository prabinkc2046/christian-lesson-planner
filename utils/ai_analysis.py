from config.ai_client import client
from config.ai_prompt import SYSTEM_PROMPT


def generate_worldview_suggestions(lesson_text):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": lesson_text},
        ],
    )

    return response.choices[0].message.content
