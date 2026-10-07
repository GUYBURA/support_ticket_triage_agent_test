import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
MODEL_NAME = os.getenv("MODEL_NAME", "openai/gpt-4o-mini")


def get_llm() -> ChatOpenAI:
    return ChatOpenAI(
        model=MODEL_NAME,
        api_key=os.environ["OPENROUTER_API_KEY"],
        base_url=OPENROUTER_BASE_URL,
    )
