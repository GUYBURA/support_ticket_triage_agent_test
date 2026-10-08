from langchain.messages import HumanMessage, SystemMessage
from src.schemas import Decision
from src.state import State
from src.config import get_llm
from src.prompts.prompts import DECIDE_PROMPT
from src.prompts.format import format_ticket

def decide(state:State) -> dict:
    llm = get_llm()
    structured_model = llm.with_structured_output(Decision)
    response = structured_model.invoke([
        SystemMessage(content=DECIDE_PROMPT),
        HumanMessage(content=(
                f"{format_ticket(state['ticket'])}\n\n"
                f"Ticket urgency: {state['ticket_urgency'].urgency}\n"
                f"Key information: {state['key_information']}\n"
                f"Ticket summary: {state['summary']}\n"
        )),
    ])
    return {"decision": response}