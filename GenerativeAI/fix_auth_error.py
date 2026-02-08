from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

load_dotenv()

# Configure ChatOpenAI to use OpenRouter
try:
    chat = ChatOpenAI(
        model="openai/gpt-3.5-turbo", # Using a common model available on OpenRouter
        api_key=os.environ.get("OPENAI_API_KEY"),
        base_url="https://openrouter.ai/api/v1"
    )
    print("Attempting to invoke model via OpenRouter...")
    response = chat.invoke("Hello, are you working?")
    print("Success!")
    print(response.content)
except Exception as e:
    print(f"Error: {e}")
