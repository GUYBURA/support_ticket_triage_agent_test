from langchain.messages import HumanMessage, SystemMessage
from src.state import State
from src.config import get_llm
from src.prompts.prompts import ESCALATE_PROMPT
from src.prompts.format import format_content

def escalate(state:State) -> dict:
    llm = get_llm()
    response = llm.invoke([
        SystemMessage(content=ESCALATE_PROMPT),
        HumanMessage(content=format_content(state))
    ])
    return {"handoff_note": response.text}