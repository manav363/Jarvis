from openai import OpenAI
import os

def ask_ai(command):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.responses.create(
        model="gpt-4o-mini",
        input=f"You are Jarvis. Keep answers short.\nUser: {command}"
    )
    return response.output_text
