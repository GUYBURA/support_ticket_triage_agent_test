from typing import Annotated, TypedDict
from src.schemas import Ticket, TicketSummary, TicketUrgency, KeyInformation, Decision
from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages

class State(TypedDict, total=False):
    messages: Annotated[list[AnyMessage], add_messages]
    ticket: Ticket
    ticket_urgency: TicketUrgency
    key_information: KeyInformation
    decision: Decision
    summary: TicketSummary
