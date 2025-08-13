import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from a .env file
# The parentheses are necessary to call the function
load_dotenv()

# Initialize the OpenAI client with the OpenRouter base URL and API key.
# os.getenv() is the correct and safe way to retrieve an environment variable.
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

# Use the correct method for chat completions: client.chat.completions.create()
# Also, the parameter for the chat messages is 'messages', not 'input'.
response = client.chat.completions.create(
    model="openai/gpt-oss-20b:free", # Changed to a common model for reliability
    messages=[
        {
            "role": "user",
            "content": "What is the capital of Nepal?"
        }
    ],
)

# The response object structure is correct, so this line will work.
print(response.choices[0].message.content)

