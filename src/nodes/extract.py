from langchain.messages import HumanMessage, SystemMessage
from src.schemas import KeyInformation
from src.state import State
from src.config import get_llm
from src.prompts.prompts import EXTRACT_PROMPT
from src.prompts.ticket import format_ticket

def extract(state:State) -> dict:
    llm = get_llm()
    structured_model = llm.with_structured_output(KeyInformation)
    response = structured_model.invoke([
    SystemMessage(content=EXTRACT_PROMPT),
    HumanMessage(content=(
        f"{format_ticket(state['ticket'])}\n\n"
        f"Ticket urgency: {state['ticket_urgency'].urgency}\n"
        )),
    ])
    return {"key_information": response}