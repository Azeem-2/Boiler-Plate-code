import os
import asyncio
from dotenv import load_dotenv
from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    set_default_openai_api,
    set_default_openai_client,
    set_tracing_disabled,
)

# Load environment variables
load_dotenv()

# Default values with fallback
BASE_URL = os.getenv("BASE_URL", "https://generativelanguage.googleapis.com/v1beta/openai/")
API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.5-flash")

# Validate required settings
if not API_KEY:
    raise ValueError("Missing GEMINI_API_KEY. Please set it in your .env file or environment.")

# Create OpenAI client
client = AsyncOpenAI(
    base_url=BASE_URL,
    api_key=API_KEY,
)

# Configure defaults
set_default_openai_client(client=client, use_for_tracing=True)
set_default_openai_api("chat_completions")
set_tracing_disabled(True)


async def main():
    """Run a simple example agent."""
    agent = Agent(
        name="Example Agent",
        instructions="You are a helpful assistant.",
        model=MODEL_NAME,
    )

    # Run agent with a sample prompt
    result = await Runner.run(agent, "Hello! How are you?")
    print("Agent Output:\n", result.final_output)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nExecution stopped by user.")
