import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME", "openai/gpt-4o-mini")


def get_llm() -> ChatOpenAI:
    if os.getenv("OPENAI_API_KEY"):
        return ChatOpenAI(
            model=MODEL_NAME,
            api_key=os.environ["OPENAI_API_KEY"]
        )
    return ChatOpenAI(
        model=MODEL_NAME,
        api_key=os.environ["OPENROUTER_API_KEY"],
        base_url=os.environ["OPENROUTER_BASE_URL"],
    )
