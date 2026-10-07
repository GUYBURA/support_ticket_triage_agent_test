from langchain.messages import HumanMessage, SystemMessage
from src.schemas import TicketUrgency
from src.state import State
from src.config import get_llm
from src.prompts.prompts import URGENCY_PROMPT
from src.prompts.ticket import format_ticket

def classify(state:State) -> dict:
    llm = get_llm()
    structured_model = llm.with_structured_output(TicketUrgency)
    response = structured_model.invoke([
        SystemMessage(content=URGENCY_PROMPT),
        HumanMessage(content=format_ticket(state["ticket"]))
    ])
    return {"ticket_urgency": response,}