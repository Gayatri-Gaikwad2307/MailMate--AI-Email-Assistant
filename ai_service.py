import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found in .env file")

client = genai.Client(api_key=api_key)


def generate_email(prompt):
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=f"""
        Write a professional and well-structured email about:
        {prompt}
        """
    )

    return response.text