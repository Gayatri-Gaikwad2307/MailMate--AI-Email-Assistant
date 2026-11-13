
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("API key loaded:", bool(api_key))

client = genai.Client(api_key=api_key)

print("\nFetching models...\n")

try:
    models = list(client.models.list())

    print("Total models found:", len(models))

    for model in models:
        print("Model:", model.name)

    if not models:
        print("No models returned by the API.")

except Exception as e:
    print("API Error:", repr(e))
