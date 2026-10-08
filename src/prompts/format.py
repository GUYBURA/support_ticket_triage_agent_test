from src.schemas import Ticket
from src.state import State

def format_ticket(ticket: Ticket) -> str:
    ticket = Ticket.model_validate(ticket)
    lines = [f"Ticket ID: {ticket.ticket_id} Customer ID: {ticket.customer_id}"]
    for i, m in enumerate(ticket.messages, start=1):
        lines.append(f"Message {i} ({m.sent_at}): {m.content}")
    return "\n".join(lines)

def format_content(state: State) -> str:
    key_info = state["key_information"]
    content = (
        f"{format_ticket(state['ticket'])}\n\n"
        f"Urgency: {state['ticket_urgency'].urgency}\n"
        f"Product: {key_info.product}\n"
        f"Issue Type: {key_info.issue_type}\n"
        f"Customer Sentiment: {key_info.customer_sentiment}\n"
        f"Summary: {state['summary']}\n"
    )
    return content