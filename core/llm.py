import os
import base64
from openai import OpenAI
from dotenv import load_dotenv
from core.memory import get_recent_history

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_response(text, image_path=None, history=None):

    messages = []

    # Get last few messages
    if history:
        history = get_recent_history(history)

        for msg in history:
            messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })

    # Add current query
    if image_path:
        with open(image_path, "rb") as img:
            base64_image = base64.b64encode(img.read()).decode()

        messages.append({
            "role": "user",
            "content": [
                {"type": "text", "text": text},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                }
            ]
        })
    else:
        messages.append({
            "role": "user",
            "content": text
        })

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    return response.choices[0].message.content