import os
from dotenv import load_dotenv
import asyncio
from agents import  Agent, Runner,AsyncOpenAI, set_default_openai_api, set_default_openai_client,set_tracing_disabled



load_dotenv()


BASE_URL = os.getenv("BASE_URL") or "https://generativelanguage.googleapis.com/v1beta/openai/"
API_KEY = os.getenv("GEMINI_API_KEY") 
MODEL_NAME = os.getenv("MODEL_NAME") or "gemini-2.5-flash"


if not BASE_URL or not API_KEY or not MODEL_NAME:
    raise ValueError("Please set BASE_URL, GEMINI_API_KEY, MODEL_NAME via env var or code.")

# Create OpenAI client
client = AsyncOpenAI(
    base_url=BASE_URL,
    api_key=API_KEY,
)

# Configure the client
set_default_openai_client(client=client, use_for_tracing=True)
set_default_openai_api("chat_completions")
set_tracing_disabled(True)


async def main():
    agent = Agent(name="Example Agent", instructions="Simple Agent", model=MODEL_NAME)
    first_result = await Runner.run(agent, "Hi")
    print(first_result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
