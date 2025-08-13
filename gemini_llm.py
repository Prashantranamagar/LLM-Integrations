
import os
from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", None)
if GEMINI_API_KEY is None:
    raise ValueError("GEMINI_API_KEY environment variable is not set.") 


from google import genai
from google.genai import types

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0) # Disables thinking, by default it enables thinking
    ),
)
print(response.text)