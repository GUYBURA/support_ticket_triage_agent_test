import json
from pathlib import Path

from langchain.tools import tool

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "knowledge_base.json"

@tool
def lookup_knowledge_base() -> str:
    """Search the support knowledge base for articles about a customer's issue.
    """
    with open(DATA_PATH, encoding="utf-8") as f:
        knowledge_base = json.load(f)
    return "\n\n".join(f"[{i['id']}] {i['title']}\n{i['content']}" for i in knowledge_base)