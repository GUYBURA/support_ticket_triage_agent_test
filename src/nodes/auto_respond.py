from langchain.messages import HumanMessage, SystemMessage
from src.state import State
from src.config import get_llm
from src.prompts.prompts import AUTO_RESPOND_PROMPT
from src.prompts.format import format_ticket

def auto_respond(state:State) -> dict:
    llm = get_llm()
    response = llm.invoke([
        SystemMessage(content=AUTO_RESPOND_PROMPT),
        HumanMessage(content=
                     f"{format_ticket(state['ticket'])}\n\n"
                     f"Summary: {state['summary']}"
                     )
    ])
    return {"customer_reply": response.text}